from typing import Optional

from app.domain.entities.restaurant import CreateMenuRequest, MenuEntity, ProductEntity
from app.services.menu_service import MenuService


class MenuUseCases:
    @staticmethod
    async def create(
            data: CreateMenuRequest
    ) -> tuple[MenuEntity, list[ProductEntity] | None]:
        menu, items = await MenuService().create_menu_with_products_and_categories(
            categories=data.categories, items=data.items
        )

        return menu, items

    @staticmethod
    async def get_menu(menu_id: int = None) -> Optional[MenuEntity]:
        menu = await MenuService().get_menu_by_id_or_last_menu(menu_id=menu_id)

        return menu
