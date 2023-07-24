from typing import List
from fastapi import APIRouter

from schema import Menu as MenuSchema
from models import Menu as MenuModel


router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Menu CRUD"]
)


@router.get("/", response_model=List[MenuSchema])
def get_menus():
    return []
