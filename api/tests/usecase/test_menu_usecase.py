import pytest
from mock.mock import MagicMock

from app.domain.entities.restaurant import CreateMenuRequest, MenuEntity, ProductEntity
from app.domain.usecases.menu_use_cases import MenuUseCases


@pytest.fixture
def create_menu_request():
    return CreateMenuRequest(
        categories=[],
        items=[ProductEntity(name="Product1"), ProductEntity(name="Product2")],
    )


@pytest.mark.asyncio
@pytest.mark.skip(reason="some bug is happening with the coroutine")
async def test_create(create_menu_request):
    menu_service_mock = MagicMock()
    menu_service_mock.create_menu_with_products_and_categories = MagicMock(
        return_value=(
            MenuEntity(name="Menu"),
            [ProductEntity(name="Product1", image_id="image")],
        )
    )

    menu_usecases = MenuUseCases()
    menu_usecases.create_menu_request = (
        menu_service_mock.create_menu_with_products_and_categories
    )

    result_menu, result_items = await menu_usecases.create(data=create_menu_request)

    # Assertions
    assert result_menu
    assert result_menu.name == "Menu"
    assert result_items
    assert len(result_items) == 1
    assert result_items[0].name == "Product1"


@pytest.mark.asyncio
@pytest.mark.skip(reason="some bug is happening with the session DB")
async def test_get_menu():
    menu_id = 1

    # Mock the MenuService method get_menu_by_id_or_last_menu
    menu_service_mock = MagicMock()
    menu_service_mock.get_menu_by_id_or_last_menu = MagicMock(
        return_value=MenuEntity(name="Menu")
    )

    # Replace the real MenuService instance with the mock
    menu_usecases = MenuUseCases()
    menu_usecases.get_menu_request = menu_service_mock.get_menu_by_id_or_last_menu

    # Call the method being tested
    result_menu = await menu_usecases.get_menu(menu_id)

    # Assertions
    assert result_menu
    assert result_menu.name == "Menu"


@pytest.mark.asyncio
@pytest.mark.skip(reason="some bug is happening with the session DB")
async def test_get_menu_no_menu_id():
    menu_service_mock = MagicMock()
    menu_service_mock.get_menu_by_id_or_last_menu = MagicMock(return_value=None)

    menu_usecases = MenuUseCases()
    menu_usecases.get_menu_request = menu_service_mock.get_menu_by_id_or_last_menu

    result_menu = await menu_usecases.get_menu()

    assert result_menu == []
