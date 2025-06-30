import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from config.loader import load_config
from backend.api import router as api_router

config = load_config()
app = FastAPI(title='My first FastAPI project', description='This api was developed by Timur Boltaboyev')

app.include_router(api_router)

# alembic - для отправления миграций в БД
# sqlalchemy - для работы с БД через классы


# class ItemModel(BaseModel):
#     title: str
#     description: str | None = None
#     price: float


# class ItemViewModel(BaseModel):
#     id: int
#     title: str
#     description: str | None = None
#     price: float

# @app.get('/items/', response_model=list[int])
# def get_items(q: str | None = None, limit: int = 5, offset: int = 0) -> list[int]:
#     print(q)
#     items = list(range(1, 101))
#     items_length = len(items)
#     return {
#         'length': items_length,
#         'items': items[offset:offset+limit]
#     }

# @app.post('/items/')
# def create_item(item: ItemModel) -> ItemModel:
#     return item

# @app.get('/items/{item_id}/')
# def get_item_detail(item_id: int) -> ItemViewModel:
#     item = {
#         'id': item_id,
#         'title': 'new title',
#         'description': 'new description',
#         'price': 12.12
#     }
#     item = ItemViewModel(**item)
#     return item

if __name__ == '__main__': # первый способ запуска проекта
    uvicorn.run('main:app', reload=True, host=config.run_api.api_host, port=config.run_api.api_port)

# fastapi dev main.py - второй способ запуска проекта

# alembic init -t async <name:file_for_migrations>
# alembic init -t async infrastructure/migrations
# alembic revision --autogenerate -m '<comment>'
# alemdic upgrade head