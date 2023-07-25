from typing import List
from fastapi import APIRouter, Depends, Response, status


from schema import MenuBase as MenuSchema, MenuResponse
from schema import Menu, MenuCreate, MenuUpdate

from services.menu_service import MenuService


router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Menu CRUD"]
)


@router.get("/", response_model=List[MenuSchema])
def get_menus(service: MenuService = Depends()):
    return service.get_list()


@router.get("/{target_menu_id}")
def get_menu(
    target_menu_id: str,
    service: MenuService = Depends()
):
    return service.get(target_menu_id)


@router.post("/", response_model=MenuResponse, status_code=status.HTTP_201_CREATED)
def create_menu(
    menu_data: MenuCreate,
    service: MenuService = Depends()
):
    return service.create(menu_data)


@router.patch("/{target_menu_id}", response_model=MenuResponse)
def update_menu(
    target_menu_id: str,
    update_data: MenuUpdate,
    service: MenuService = Depends()
):
    return service.update(target_menu_id, update_data)


@router.delete("/{target_menu_id}")
def delete_menu(
    target_menu_id: str,
    service: MenuService = Depends()
):
    return service.delete(target_menu_id)

