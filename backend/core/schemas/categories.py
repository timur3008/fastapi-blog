from typing import Optional
from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int
    name: str
    icon: Optional[str]


class CategoryCreateschema(BaseModel):
    name: str
    icon: Optional[str] = None


class CategoryUpdateSchema(BaseModel):
    name: Optional[str] = None
    icon: Optional[str] = None