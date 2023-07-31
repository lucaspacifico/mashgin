from typing import List

from app.infrastructure.orm_base import get_session
from app.models.restaurant_models import Product as ProductModel
from app.domain.entities.restaurant import ProductEntity
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession


class ProductRepository:
    def __init__(self):
        self.model_cls = ProductModel
        self.session = get_session()

    @staticmethod
    async def create(
        session: AsyncSession, data_orm: List[ProductModel]
    ) -> List[ProductModel]:
        session.add_all(data_orm)
        await session.flush()

        return data_orm

    async def bulk_add(self, data: List[ProductEntity]) -> List[ProductEntity]:
        list_product_orm = [
            self.model_cls(**product.model_dump(exclude_none=True)) for product in data
        ]

        async with self.session.begin() as session:
            response_list_product_orm: List[ProductModel] = await self.create(
                session, list_product_orm
            )

        return [
            ProductEntity.model_validate(product_orm)
            for product_orm in response_list_product_orm
        ]

    async def get_by_ids(self, products_ids: List[int]) -> List[int]:
        async with self.session.begin() as session:
            statement = select(ProductModel.id).where(ProductModel.id._in(products_ids))
            menu_orm = await session.execute(statement)
        result = menu_orm.scalars().one()

        return result