from typing import List
from fastapi import APIRouter, Depends, Response, status


from schema import MenuBase as MenuSchema
from schema import Menu, MenuCreate, MenuUpdate

from services.menu_service import MenuService


router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Menu CRUD"]
)


@router.get("/", response_model=List[MenuSchema])
def get_menus(service: MenuService = Depends()):
    return service.get_list()


@router.get("/{target_menu_id}", response_model=MenuSchema)
def get_menu(
    target_menu_id: str,
    service: MenuService = Depends()
):
    return service.get(target_menu_id)


@router.post("/", response_model=MenuCreate)
def create_menu(
    menu_data: MenuCreate,
    service: MenuService = Depends()
):
    return service.create(menu_data)


@router.patch("/{target_menu_id}", response_model=MenuSchema)
def update_menu(
    target_menu_id: str,
    update_data: MenuUpdate,
    service: MenuService = Depends()
):
    return service.update(target_menu_id, update_data)


@router.delete("/{target_menu_id}", response_model=Menu)
def delete_menu(
    target_menu_id: str,
    service: MenuService = Depends()
):
    service.delete(target_menu_id)
    return Response(status_code=status.HTTP_200_OK)
