from fastapi import APIRouter

from api.menu_router import router as menu_router
from api.submenu_router import router as submenu_router
from api.dish_router import router as dish_router


router = APIRouter()

router.include_router(menu_router)
router.include_router(submenu_router)
router.include_router(dish_router)
