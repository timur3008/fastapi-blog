from .base import BaseRepo

import sqlalchemy as sa
from infrastructure.database.models import Category


class CategoryRepo(BaseRepo):
    async def get_categories(self):
        query = sa.select(Category)
        result = await self.session.execute(query)
        return result.scalars().all() # -> [(), (), ()]
    
    async def insert_category(self, name: str, icon: str | None = None):
        query = sa.insert(Category).values(name=name, icon=icon).returning(Category)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one()
    
    async def get_category_detail(self, category_id: int):
        query = sa.select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    
    async def update_category(self, category_id: int, category_data: dict):
        query = sa.update(Category).where(Category.id == category_id).values(**category_data).returning(Category)
        updated = await self.session.execute(query)
        await self.session.commit()
        return updated.scalar_one_or_none()
    
    async def delete_category(self, category_id: int):
        query = sa.delete(Category).where(Category.id == category_id).returning(Category)
        deleted = await self.session.execute(query)
        await self.session.commit()
        return deleted.scalar_one_or_none()