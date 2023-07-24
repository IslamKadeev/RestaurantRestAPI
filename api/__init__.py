from fastapi import APIRouter

from api.menu_router import router as menu_router


router = APIRouter()

router.include_router(menu_router)
