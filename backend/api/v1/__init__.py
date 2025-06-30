from fastapi import APIRouter

from .routes.categories import router as categories_router
from .routes.products import router as products_router
from backend.app.config import config


router = APIRouter(prefix=config.api_prefix.v1.prefix)

router.include_router(categories_router)
router.include_router(products_router)