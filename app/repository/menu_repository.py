from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.restaurant import MenuEntity
from app.infrastructure.orm_base import get_session
from app.models.restaurant_models import Menu as MenuModel


class MenuRepository:
    def __init__(self):
        self.model_cls = MenuModel
        self.session = get_session()

    @staticmethod
    async def create(session: AsyncSession, data_orm: MenuModel) -> MenuModel:
        session.add(data_orm)
        await session.flush()

        return data_orm

    async def add(self, data: MenuEntity) -> MenuEntity:
        menu_model = self.model_cls(**data.model_dump(exclude_none=True))

        async with self.session.begin() as session:
            menu_orm: MenuModel = await self.create(session, menu_model)
        return MenuEntity.model_validate(menu_orm)

    async def get_by_id(self, menu_id: int):
        async with self.session.begin() as session:
            statement = select(MenuModel).where(MenuModel.id == menu_id)

            menu_orm = await session.execute(statement)
        result = menu_orm.scalars().one()

        return MenuEntity.model_validate(result)

    async def last_menu(self):
        async with self.session.begin() as session:
            statement = select(MenuModel).order_by(desc(MenuModel.created_at)).limit(1)

            menu_orm = await session.execute(statement)
        result = menu_orm.scalars().one()

        return MenuEntity.model_validate(result)
