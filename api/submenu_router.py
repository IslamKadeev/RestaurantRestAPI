from typing import List
import uuid
from fastapi import APIRouter, Depends, Response, status
from schema import SubmenuCreate, SubmenuResponse, SubmenuUpdate

from services.submenu_service import SubmenuService


router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Submenu CRUD"]
)


@router.get("/{target_menu_id}/submenus", response_model=List[SubmenuResponse])
def get_submenus(
    service: SubmenuService = Depends()
):
    return service.get_list()


@router.get("/{target_menu_id}/submenus/{target_submenu_id}", response_model=SubmenuResponse)
def get_submenu(
    target_submenu_id: str,
    service: SubmenuService = Depends()
):
    return service.get(target_submenu_id)


@router.post(
    '/{target_menu_id}/submenus',
    status_code=status.HTTP_201_CREATED,
    response_model=SubmenuResponse)
def create_submenu(
    target_menu_id: str,
    submenu_data: SubmenuCreate,
    service: SubmenuService = Depends()
):
    return service.create(target_menu_id, submenu_data)


@router.patch("/{target_menu_id}/submenus/{target_submenu_id}", response_model=SubmenuResponse)
def update_submenu(
    target_submenu_id: str,
    update_data: SubmenuUpdate,
    service: SubmenuService = Depends()
):
    return service.update(target_submenu_id, update_data)


@router.delete("/{target_menu_id}/submenus/{target_submenu_id}")
def delete_submenu(
    target_submenu_id: str,
    service: SubmenuService = Depends()
):
    return service.delete(target_submenu_id)