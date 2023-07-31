from typing import List

from sqlalchemy.exc import NoResultFound

from app.domain.entities.restaurant import (
    ProductEntity,
    OrderEntity,
    PaymentEntity,
)
from app.infrastructure.logger import Logger
from app.repository.order_repository import OrderRepository
from app.repository.payment_repository import PaymentRepository
from app.repository.product_repository import ProductRepository
from app.services.product_service import ProductService
from app.settings import Settings

settings = Settings()
log = Logger(class_name=__name__)


class OrderService:

    async def create_order_with_payment(
        self, payment_form: PaymentEntity, products_ids: List[int]
    ) -> OrderEntity:
        payment = await self.get_or_create_payment(payment_form=payment_form)

        products_id = self.validate_products_ids(products_ids)

        order = OrderEntity(
            payment_form=str(payment.id),
            products=products_id,
            price=payment.value
        )

        log.info(f"Creating order {order} with payment {payment.id}")
        return await OrderRepository().add(data=order)


    @staticmethod
    async def get_order_by_id_or_last_order(order_id: int):
        try:
            if order_id:
                return await OrderRepository().get_by_id(order_id=order_id)
            return await OrderRepository().last_order()
        except NoResultFound:
            return []

    @staticmethod
    async def get_or_create_payment(payment_form: PaymentEntity) -> PaymentEntity:
        if payment_form.id:
            return await PaymentRepository().get_by_id(payment_id=payment_form.id)

        return await PaymentRepository().add(data=payment_form)

    @staticmethod
    def validate_products_ids(products_id: List[int]) -> List[int]:
        validated_products_id = await ProductService.validate_products(products_id=products_id)

        return validated_products_id