from fastapi import APIRouter, HTTPException, status
from fastapi.exceptions import ValidationException
from pydantic import ValidationError

from app.const import ORDER_GET_DESCRIPTION
from app.domain.entities.restaurant import CreateOrderRequest
from app.domain.usecases.order_use_cases import OrderUseCases

order_router = APIRouter()


@order_router.post("/order/create", tags=["Order"])
async def create_order(request: CreateOrderRequest):
    try:
        order = await OrderUseCases().create(data=request)
    except (ValidationError, ValidationException) as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not create menu, wrong arguments -- {str(exception)}",
        )

    return {"message": "Order created successfully", "data": order}


@order_router.get(
    "/order/{order_id}", tags=["Order"], description=ORDER_GET_DESCRIPTION
)
async def get_order(order_id: int):
    result = await OrderUseCases().get_order(order_id=order_id)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order Not Found",
        )

    return {"data": result}
