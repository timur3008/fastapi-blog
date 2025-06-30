import sqlalchemy as sa
from sqlalchemy.orm import selectinload

from infrastructure.database.repo.base import BaseRepo
from infrastructure.database.models import Product


class ProductRepo(BaseRepo):
    async def get_products(self):
        query = sa.select(Product).options(selectinload(Product.category))
        result = await self.session.execute(query)
        return result.scalars().all()
    
    async def create_product(self, name: str, price: float, category_id: int, description: str | None = None, quantity: int = 5, in_stock: bool = True):
        query = (
            sa.insert(Product).values(name=name, description=description, quantity=quantity, in_stock=in_stock, price=price, category_id=category_id)
            .options(selectinload(Product.category))
            .returning(Product)
        )
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one()
    
    async def get_product_detail(self, product_id: int):
        query = sa.select(Product).where(Product.id == product_id).options(selectinload(Product.category))
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    async def update_product(self, product_id: int, product_data: dict):
        query = sa.update(Product).values(**product_data).where(Product.id == product_id).options(selectinload(Product.category)).returning(Product)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one_or_none()

    async def delete_product(self, product_id: int):
        query = sa.delete(Product).where(Product.id == product_id).options(selectinload(Product.category)).returning(Product)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one_or_none()