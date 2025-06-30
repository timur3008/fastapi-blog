from typing import Annotated

from backend.app.config import config
from backend.app.dependencies import get_repo
from backend.core.schemas.categories import CategorySchema, CategoryCreateschema, CategoryUpdateSchema
from infrastructure.database.repo.requests import RequestsRepo

from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix=config.api_prefix.v1.categories, tags=['Categories'])


@router.get('/')
async def get_all_categories(repo: Annotated[RequestsRepo, Depends(get_repo)]) -> list[CategorySchema]:
    return await repo.categories.get_categories()

@router.post('/')
async def create_category(category_data: CategoryCreateschema, repo: Annotated[RequestsRepo, Depends(get_repo)]) -> CategorySchema:
    new_category = await repo.categories.insert_category(name=category_data.name, icon=category_data.icon)
    return new_category

@router.get('/{category_id}')
async def get_category_detail(category_id: int, repo: Annotated[RequestsRepo, Depends(get_repo)]) -> CategorySchema:
    category = await repo.categories.get_category_detail(category_id=category_id)

    if category is None:
        raise HTTPException(status_code=404, detail=f'Category with {category_id=} not found')
    return category

@router.patch('/{category_id}')
async def update_category(category_id: int, category_data: CategoryUpdateSchema, repo: Annotated[RequestsRepo, Depends(get_repo)]) -> CategorySchema:
    data = {k: v for (k, v) in category_data.dict().items() if v is not None}
    updated = await repo.categories.update_category(category_id=category_id, category_data=data)

    if updated is None:
        raise HTTPException(status_code=404, detail=f'Category with {category_id=} not found')
    return updated

@router.delete('/{category_id}')
async def delete_category(category_id: int, repo: Annotated[RequestsRepo, Depends(get_repo)]) -> CategorySchema:
    deleted = await repo.categories.delete_category(category_id=category_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail=f'Category with {category_id=} not found')
    return deleted