from typing import List, Any, Tuple

from sqlalchemy.exc import NoResultFound

from app.domain.entities.restaurant import CategoryEntity, MenuEntity, ProductEntity
from app.infrastructure.logger import Logger
from app.repository.category_repository import CategoryRepository
from app.repository.menu_repository import MenuRepository
from app.repository.product_repository import ProductRepository
from app.settings import Settings

settings = Settings()
log = Logger(class_name=__name__)


class MenuService:
    @staticmethod
    async def create_menu(
        categories: List[CategoryEntity], name: str = None
    ) -> MenuEntity:
        menu = MenuEntity(
            categories_id=[category.id for category in categories],
            name=name if name else settings.menu_name,
        )

        log.info(f"Creating menu {menu}")
        return await MenuRepository().add(data=menu)

    async def create_menu_with_products_and_categories(
        self, categories: List[CategoryEntity], items: List[ProductEntity] = None
    ) -> tuple[MenuEntity, list[ProductEntity] | None]:
        categories = await self.create_categories(categories=categories)
        if items:
            items = await self.create_products(items=items)

        log.info(f"Created categories: {categories} with {items}")

        menu = await self.create_menu(categories=categories)

        return menu, items

    @staticmethod
    async def create_categories(
        categories: List[CategoryEntity],
    ) -> List[CategoryEntity]:
        return await CategoryRepository().bulk_add(data=categories)

    @staticmethod
    async def create_products(items: List[ProductEntity]) -> List[ProductEntity]:
        return await ProductRepository().bulk_add(items)

    @staticmethod
    async def get_menu_by_id_or_last_menu(menu_id: int) -> list[Any] | tuple[
        Any, list[ProductEntity]]:
        try:
            if menu_id:
                menu = await MenuRepository().get_by_id(menu_id=menu_id)
            else:
                menu = await MenuRepository().last_menu()
        except NoResultFound:
            return []

        categories = await CategoryRepository().get_by_categories_id(categories_id=menu.categories_id)
        products = await ProductRepository().get_products_by_categories_id(categories_id=menu.categories_id)
        return categories, products