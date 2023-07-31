from typing import Generator

import pytest
import pytest_asyncio
from sqlalchemy import create_engine, event, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.infrastructure.orm_base import Base
from app.settings import Settings

settings = Settings()


@pytest.fixture(scope="session")
def setup_db() -> Generator:
    engine = create_engine(
        f"postgresql://{settings.mashgin_db_user}:{settings.mashgin_db_password}"
        f"@{settings.mashgin_db_host}:{settings.mashgin_db_port}"
        f"/{settings.mashgin_db_name}"
    )
    conn = engine.connect()

    conn.execute(text("commit"))

    try:
        conn.execute(text("drop database test"))
    except SQLAlchemyError:
        pass
    finally:
        conn.close()

    conn = engine.connect()

    conn.execute(text("commit"))
    conn.execute(text("create database test"))
    conn.close()

    yield

    conn = engine.connect()

    conn.execute(text("commit"))
    try:
        conn.execute(text("drop database test"))
    except SQLAlchemyError:
        pass
    conn.close()


@pytest.fixture(scope="session")
def engine():
    __db_uri = (
        f"postgresql://{settings.mashgin_db_user}:{settings.mashgin_db_password}"
        f"@{settings.mashgin_db_host}:{settings.mashgin_db_port}/{settings.mashgin_db_name}"
    )
    engine = create_engine(
        __db_uri,
        pool_pre_ping=True,
        echo=True,
    )

    return engine


@pytest.fixture(scope="session", autouse=True)
def setup_test_db(engine):

    with engine.begin():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        yield
        Base.metadata.drop_all(engine)


@pytest.mark.asyncio
@pytest_asyncio.fixture(scope="session")
async def session():
    # https://github.com/sqlalchemy/sqlalchemy/issues/5811#issuecomment-756269881
    async_engine = create_async_engine(
        f"postgresql+asyncpg://{settings.mashgin_db_user}:{settings.mashgin_db_password}"
        f"@{settings.mashgin_db_host}:{settings.mashgin_db_port}/{settings.mashgin_db_name}",
        pool_pre_ping=True,
        echo=False,
    )
    async with async_engine.connect() as conn:
        await conn.begin()
        await conn.begin_nested()
        AsyncSessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=conn,
            future=True,
            class_=AsyncSession,
        )

        async_session = AsyncSessionLocal()

        @event.listens_for(async_session.sync_session, "after_transaction_end")
        def end_savepoint(session, transaction):
            if conn.closed:
                return
            if not conn.in_nested_transaction:
                conn.sync_connection.begin_nested()

        def test_get_session() -> Generator:
            try:
                yield AsyncSessionLocal
            except SQLAlchemyError:
                pass

        # app.dependency_overrides[async_session_local] = test_get_session

        yield async_session
        await async_session.close()
        await conn.rollback()
