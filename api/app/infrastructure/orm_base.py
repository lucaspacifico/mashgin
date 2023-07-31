from urllib.parse import quote_plus

from sqlalchemy import MetaData
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from app.infrastructure.logger import Logger
from app.settings import Settings

settings = Settings()
log = Logger(__name__)

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)
_Base = declarative_base(metadata=metadata)

async_engine = create_async_engine(
    f"postgresql+asyncpg://{settings.mashgin_db_user}:{settings.mashgin_db_password}"
    f"@{settings.mashgin_db_host}:{settings.mashgin_db_port}/{settings.mashgin_db_name}",
    pool_pre_ping=True,
    echo=settings.mashgin_db_echo_sql,
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
)


def create_db_uri(
    mashgin_db_user: str,
    mashgin_db_password: str,
    mashgin_db_host: str,
    mashgin_db_port: int,
    mashgin_db_name: str,
) -> str:
    db_uri = (
        f"postgresql+asyncpg://{mashgin_db_user}:"
        + f"{quote_plus(mashgin_db_password)}@{mashgin_db_host}:"
        + f"{mashgin_db_port}/"
        + f"{mashgin_db_name}"
    )

    db_uri = db_uri.replace("%", "%%")

    return db_uri


def get_session():
    try:
        return AsyncSessionLocal
    except SQLAlchemyError as e:
        log.exception(e)


class Base(_Base):
    __abstract__ = True

    def __repr__(self):
        columns = ", ".join(
            [
                f"{k}={repr(v)}"
                for k, v in self.__dict__.items()
                if not k.startswith("_")
            ]
        )
        return f"<{self.__class__.__name__}({columns})>"
