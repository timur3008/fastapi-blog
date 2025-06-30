from typing import Optional
from pydantic import BaseModel

from backend.core.schemas.categories import CategorySchema


class ProductSchema(BaseModel):
    id: int
    name: str
    description: str | None
    quantity: int
    price: float
    in_stock: bool
    category: CategorySchema


class ProductCreateSchema(BaseModel):
    name: str
    price: float
    category_id: int
    description: str | None = None
    quantity: int = 5
    in_stock: bool = True


class ProductUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    in_stock: Optional[bool] = None


class ProductDeleteSchema(BaseModel):
    is_deleted: bool