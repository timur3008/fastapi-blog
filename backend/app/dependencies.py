from infrastructure.database.repo.requests import RequestsRepo
from infrastructure.database.setup import create_engine, create_session_pool
from backend.app.config import config

engine = create_engine(db=config.db)
session_pool = create_session_pool(engine=engine)

async def get_repo() -> RequestsRepo: # type: ignore
    async with session_pool() as session:
        yield RequestsRepo(session=session)