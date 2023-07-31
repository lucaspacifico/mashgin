from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.restaurant import PaymentEntity
from app.infrastructure.orm_base import get_session
from app.models.restaurant_models import Payment as PaymentModel


class PaymentRepository:
    def __init__(self):
        self.model_cls = PaymentModel
        self.session = get_session()

    @staticmethod
    async def create(session: AsyncSession, data_orm: PaymentModel) -> PaymentModel:
        session.add(data_orm)
        await session.flush()

        return data_orm

    async def add(self, data: PaymentEntity) -> PaymentEntity:
        payment_model = self.model_cls(**data.model_dump(exclude_none=True))

        async with self.session.begin() as session:
            payment_orm: PaymentModel = await self.create(session, payment_model)
        return PaymentEntity.model_validate(payment_orm)

    async def get_by_id(self, payment_id: int) -> PaymentEntity:
        async with self.session.begin() as session:
            statement = select(PaymentModel).where(PaymentModel.id == payment_id)

            payment_orm = await session.execute(statement)
        result = payment_orm.scalars().one()

        return PaymentEntity.model_validate(result)
