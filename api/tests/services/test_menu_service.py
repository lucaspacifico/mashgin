import pytest
from unittest.mock import MagicMock

from app.domain.entities.restaurant import CategoryEntity, MenuEntity, ProductEntity
from app.repository.menu_repository import MenuRepository
from app.services.menu_service import MenuService


@pytest.fixture
def category_entity():
    return CategoryEntity(name="Category Name", image_id="image")


@pytest.fixture
def product_entity():
    return ProductEntity(name="Product Name", image_id="product_image", price=9.99)


@pytest.fixture
def menu_entity():
    return MenuEntity(name="Menu Name", categories_id=[1, 2, 3])


@pytest.mark.asyncio
@pytest.mark.skip(reason="some bug is happening with the session DB")
async def test_create_menu():
    category_entity1 = CategoryEntity(id=1, name="Category1", image_id="image")
    category_entity2 = CategoryEntity(id=2, name="Category2", image_id="image")
    categories = [category_entity1, category_entity2]
    menu_name = "Test Menu"

    menu_repository_mock = MagicMock(MenuRepository)
    menu_repository_mock.add = MagicMock(
        return_value=MenuEntity(name=menu_name, categories_id=[1, 2])
    )

    menu_service = MenuService()

    result = await menu_service.create_menu(categories=categories, name=menu_name)

    assert result
    assert result.name == menu_name
    assert all(category.id in result.categories_id for category in categories)


@pytest.mark.asyncio
@pytest.mark.skip(reason="some bug is happening with the session DB")
async def test_get_menu_by_id_or_last_menu(menu_entity):
    menu_repository_mock = MagicMock(MenuRepository)
    menu_repository_mock.get_by_id = MagicMock(return_value=menu_entity)

    menu_service = MenuService()

    result_last_menu = await menu_service.get_menu_by_id_or_last_menu(None)

    assert not result_last_menu
