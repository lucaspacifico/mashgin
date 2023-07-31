from typing import List

from app.repository.product_repository import ProductRepository


class ProductService:

    @staticmethod
    async def validate_products(products_id: List[int]):
        return await ProductRepository.get_by_ids(products_id)
