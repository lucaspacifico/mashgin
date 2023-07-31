from typing import List

from app.repository.product_repository import ProductRepository


class ProductService:
    @staticmethod
    async def validate_products(product_ids: List[int]) -> List[int]:
        return await ProductRepository().get_by_ids(product_ids=product_ids)
