from typing import Optional

from app.domain.entities.restaurant import CreateOrderRequest, OrderEntity
from app.services.order_service import OrderService


class OrderUseCases:
    async def create(self, data: CreateOrderRequest) -> OrderEntity:

        order = await OrderService().create_order_with_payment(
            payment_form=data.payment_form, products_ids=data.products
        )

        return order

    async def get_order(self, order_id: int = None) -> Optional[OrderEntity]:
        order = await OrderService().get_order_by_id_or_last_order(order_id=order_id)

        return order
