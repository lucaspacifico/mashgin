from datetime import datetime

from sqlalchemy import Column, DateTime, func

from app.infrastructure.orm_base import Base


class BaseDateTime(Base):
    __abstract__ = True

    created_at = Column(DateTime, nullable=True, default=datetime.now, index=True)
    updated_at = Column(DateTime, nullable=True, onupdate=func.now(), index=True)
