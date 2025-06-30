from typing import Annotated

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.schemas.products import ProductSchema, ProductCreateSchema, ProductUpdateSchema, ProductDeleteSchema
from infrastructure.database.repo.requests import RequestsRepo

from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix=config.api_prefix.v1.products, tags=['Products'])


@router.get('/')
async def get_all_products(repo: Annotated[RequestsRepo, Depends(get_repo)]) -> list[ProductSchema]:
    products = await repo.products.get_products()
    return products

@router.get('/{product_id}')
async def get_product_detail(product_id: int, repo: Annotated[RequestsRepo, Depends(get_repo)]) -> ProductSchema:
    product = await repo.products.get_product_detail(product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail=f'No product with {product_id=}')
    return product

@router.post('/create')
async def create_product(product_data: ProductCreateSchema, repo: Annotated[RequestsRepo, Depends(get_repo)]) -> ProductSchema:
    new_product = await repo.products.create_product(
        name=product_data.name,
        description=product_data.description,
        quantity=product_data.quantity,
        price=product_data.price,
        in_stock=product_data.in_stock,
        category_id=product_data.category_id   
    )
    return new_product

@router.patch('/update/{product_id}')
async def update_product(product_id: int, product_data: ProductUpdateSchema, repo: Annotated[RequestsRepo, Depends(get_repo)]) -> ProductSchema:
    data = {k: v for (k, v) in product_data.dict().items() if v is not None}
    updated_product = await repo.products.update_product(product_id=product_id, product_data=data)

    if not update_product:
        raise HTTPException(status_code=404, detail=f'No product with {product_id=}')
    return updated_product

@router.delete('/delete/{product_id}')
async def delete_product(product_id: int, repo: Annotated[RequestsRepo, Depends(get_repo)]) -> ProductSchema:
    deleted_product = await repo.products.delete_product(product_id=product_id)
    
    if not deleted_product:
        raise HTTPException(status_code=404, detail=f'No product with {product_id=}')
    return deleted_product