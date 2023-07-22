from fastapi import APIRouter

from api.v1.menu.route import router as menu_router
from api.v1.submenu.route import router as submenu_router
from api.v1.dish.route import router as dish_router


from uuid import uuid4


router = APIRouter()

router.include_router(menu_router)
router.include_router(submenu_router)
router.include_router(dish_router)


def generate_uuid():
    return str(uuid4())
