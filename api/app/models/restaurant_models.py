from sqlalchemy import ARRAY, BigInteger, Column, Integer, Numeric, String
from sqlalchemy.ext.mutable import MutableList

from app.infrastructure.orm_base import Base
from app.models.base import BaseDateTime


class Product(BaseDateTime):
    __tablename__ = "product"

    id = Column(
        BigInteger(),
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True,
    )
    name: str = Column(String, nullable=False, index=True)
    image_id: str = Column(String, nullable=False)
    price = Column(Numeric(precision=10, scale=2))
    category_id: int = Column(Integer, nullable=False)


class Order(BaseDateTime):
    __tablename__ = "order"

    id = Column(
        BigInteger(),
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True,
    )
    price = Column(Numeric(precision=10, scale=2))
    payment_method_id = Column(String, nullable=False)
    products_id = Column(MutableList.as_mutable(ARRAY(Integer)))


class Payment(BaseDateTime):
    __tablename__ = "payment"

    id = Column(
        BigInteger(),
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True,
    )
    payment_method: str = Column(String, nullable=False)
    acquirer: str = Column(String, nullable=True)
    bank: str = Column(String, nullable=True)
    value = Column(Numeric(precision=10, scale=2))


class Menu(BaseDateTime):
    __tablename__ = "menu"

    id = Column(
        BigInteger(),
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True,
    )
    name: str = Column(String, nullable=False)
    categories_id = Column(MutableList.as_mutable(ARRAY(Integer)))


class Category(Base):
    __tablename__ = "category"

    id = Column(
        BigInteger(),
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True,
    )
    name: str = Column(String, nullable=False)
    image_id: str = Column(String, nullable=False)
