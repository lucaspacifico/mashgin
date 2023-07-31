from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from app.settings import Settings

settings = Settings()


# Base Entities


class ProductEntity(BaseModel):
    id: int = Field(default=None)
    name: str
    image_id: str
    price: float

    model_config = ConfigDict(from_attributes=True)


class PaymentEntity(BaseModel):
    id: int = Field(default=None)
    payment_method: str = None
    acquirer: Optional[str] = None
    bank: Optional[str] = None
    value: float

    model_config = ConfigDict(from_attributes=True)


class OrderEntity(BaseModel):
    id: int = Field(default=None)
    price: float
    payment_method_id: str
    products_id: List[int] = []

    model_config = ConfigDict(from_attributes=True)


class CategoryEntity(BaseModel):
    id: int = Field(default=None)
    name: str
    image_id: str

    model_config = ConfigDict(from_attributes=True)


class MenuEntity(BaseModel):
    id: int = Field(default=None)
    name: str
    categories_id: List[int] = []

    model_config = ConfigDict(from_attributes=True)


# REST Contracts


class CreateOrderRequest(BaseModel):
    payment_form: PaymentEntity
    products_ids: List[int]


class CreateMenuRequest(BaseModel):
    categories: List[CategoryEntity]
    items: List[ProductEntity]
