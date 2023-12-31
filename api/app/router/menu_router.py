from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from app.const import MENU_GET_DESCRIPTION
from app.domain.entities.restaurant import CreateMenuRequest
from app.domain.usecases.menu_use_cases import MenuUseCases
from app.infrastructure.logger import Logger

menu_router = APIRouter()
log = Logger(class_name=__name__)


@menu_router.post("/menu/create", tags=["Menu"])
async def create_menu(request: CreateMenuRequest):
    try:
        menu, items = await MenuUseCases().create(data=request)
    except (ValidationError, IntegrityError) as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not create menu, wrong arguments -- {str(exception)}",
        )

    return {
        "message": "Menu created successfully",
        "data": {"menu": menu, "items": items},
    }


@menu_router.get("/menu/{menu_id}", tags=["Menu"], description=MENU_GET_DESCRIPTION)
async def get_menu(menu_id: int):
    categories, products = await MenuUseCases().get_menu(menu_id=menu_id)

    if not categories:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Menu Not Found",
        )

    return {"categories": categories, "items": products}
