from typing import List

from fastapi.exceptions import ValidationException
from sqlalchemy.exc import NoResultFound

from app.domain.entities.restaurant import OrderEntity, PaymentEntity
from app.infrastructure.logger import Logger
from app.repository.order_repository import OrderRepository
from app.repository.payment_repository import PaymentRepository
from app.services.product_service import ProductService
from app.settings import Settings

settings = Settings()
log = Logger(class_name=__name__)


class OrderService:
    async def create_order_with_payment(
        self, payment_form: PaymentEntity, product_ids: List[int]
    ) -> OrderEntity:
        payment = await self.get_or_create_payment(payment_form=payment_form)

        is_valid = await self.is_valid_product_ids(product_ids)

        if not is_valid:
            raise ValidationException("Invalid product_id")

        order = OrderEntity(
            payment_method_id=str(payment.id),
            products_id=product_ids,
            price=payment.value,
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
    async def get_all_orders():
        try:
            return await OrderRepository().get_all_orders()
        except NoResultFound:
            return []


    @staticmethod
    async def get_or_create_payment(payment_form: PaymentEntity) -> PaymentEntity:
        if payment_form.id:
            return await PaymentRepository().get_by_id(payment_id=payment_form.id)

        return await PaymentRepository().add(data=payment_form)

    @staticmethod
    async def is_valid_product_ids(product_ids: List[int]) -> bool:
        existing_products_id = await ProductService.validate_products(
            product_ids=product_ids
        )

        set_existing_products_id = set(existing_products_id)
        set_product_ids = set(product_ids)

        return set_product_ids.issubset(set_existing_products_id)
