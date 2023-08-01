import pytest

from app.domain.entities.restaurant import ProductEntity
from app.repository.product_repository import ProductRepository


@pytest.fixture
def product_entity():
    return ProductEntity(
        name="Some Name",
        image_id="some_image_id",
        price=16.6

    )


@pytest.mark.asyncio
@pytest.mark.skip(reason="some bug is happening with the session DB")
async def test_create_product_entity(product_entity):
    expected_result = product_entity

    result = await ProductRepository().bulk_add([product_entity])

    assert result
    assert result[0].id
    assert result[0].name == expected_result.name


@pytest.mark.asyncio
async def test_get_by_ids(product_entity):
    created_product = await ProductRepository().bulk_add([product_entity])

    product_ids = [created_product[0].id]
    result = await ProductRepository().get_by_ids(product_ids)

    assert result
    assert len(result) == 1
    assert result[0] == created_product[0].id


@pytest.mark.asyncio
@pytest.mark.skip(reason="some bug is happening with the session DB")
async def test_get_by_ids_nonexistent(product_entity):
    created_product = await ProductRepository().bulk_add([product_entity])

    product_ids = [created_product[0].id + 1]  # Assuming the ID doesn't exist
    result = await ProductRepository().get_by_ids(product_ids)

    assert result == []  # The result should be an empty list since the ID doesn't exist