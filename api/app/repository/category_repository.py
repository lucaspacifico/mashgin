from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.restaurant import CategoryEntity
from app.infrastructure.orm_base import get_session
from app.models.restaurant_models import Category as CategoryModel


class CategoryRepository:
    def __init__(self):
        self.model_cls = CategoryModel
        self.session = get_session()

    @staticmethod
    async def create(
        session: AsyncSession, data_orm: List[CategoryModel]
    ) -> List[CategoryModel]:
        session.add_all(data_orm)
        await session.flush()

        return data_orm

    async def bulk_add(self, data: List[CategoryEntity]) -> List[CategoryEntity]:
        list_category_orm = [
            self.model_cls(**category.model_dump(exclude_none=True))
            for category in data
        ]

        async with self.session.begin() as session:
            response_list_category_orm: List[CategoryModel] = await self.create(
                session, list_category_orm
            )

        return [
            CategoryEntity.model_validate(category_orm)
            for category_orm in response_list_category_orm
        ]
