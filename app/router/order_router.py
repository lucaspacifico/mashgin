from fastapi import APIRouter

from app.const import ORDER_GET_DESCRIPTION
from app.domain.entities.restaurant import CreateOrderRequest

order_router = APIRouter()


@order_router.post("/order/create", tags=["Order"])
def create_order(request: CreateOrderRequest):
    return {"message": "Order created successfully"}


@order_router.get(
    "/order/{order_id}", tags=["Order"], description=ORDER_GET_DESCRIPTION
)
def get_order(order_id: int):
    return {"order_id": order_id}
