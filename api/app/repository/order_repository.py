from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.restaurant import OrderEntity
from app.infrastructure.orm_base import get_session
from app.models.restaurant_models import Order as OrderModel


class OrderRepository:
    def __init__(self):
        self.model_cls = OrderModel
        self.session = get_session()

    @staticmethod
    async def create(session: AsyncSession, data_orm: OrderModel) -> OrderModel:
        session.add(data_orm)
        await session.flush()

        return data_orm

    async def add(self, data: OrderEntity) -> OrderEntity:
        order_model = self.model_cls(**data.model_dump(exclude_none=True))

        async with self.session.begin() as session:
            order_orm: OrderModel = await self.create(session, order_model)
        return OrderEntity.model_validate(order_orm)

    async def get_by_id(self, order_id: int) -> OrderEntity:
        async with self.session.begin() as session:
            statement = select(OrderModel).where(OrderModel.id == order_id)

            order_orm = await session.execute(statement)
        result = order_orm.scalars().one()

        return OrderEntity.model_validate(result)

    async def last_order(self) -> OrderEntity:
        async with self.session.begin() as session:
            statement = (
                select(OrderModel).order_by(desc(OrderModel.created_at)).limit(1)
            )

            order_orm = await session.execute(statement)
        result = order_orm.scalars().one()

        return OrderEntity.model_validate(result)
