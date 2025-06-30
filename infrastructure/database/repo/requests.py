from .categories import CategoryRepo
from .products import ProductRepo

from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class RequestsRepo:
    session: AsyncSession

    @property # обращаться к методоам без скобок
    def categories(self) -> CategoryRepo:
        return CategoryRepo(session=self.session)
    
    @property
    def products(self) -> ProductRepo:
        return ProductRepo(session=self.session)