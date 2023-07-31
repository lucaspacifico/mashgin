from typing import Optional

from app.domain.entities.restaurant import CreateOrderRequest, OrderEntity
from app.services.order_service import OrderService


class OrderUseCases:
    @staticmethod
    async def create(data: CreateOrderRequest) -> OrderEntity:
        order = await OrderService().create_order_with_payment(
            payment_form=data.payment_form, product_ids=data.products_ids
        )

        return order

    @staticmethod
    async def get_order(order_id: int = None) -> Optional[OrderEntity]:
        order = await OrderService().get_order_by_id_or_last_order(order_id=order_id)

        return order
