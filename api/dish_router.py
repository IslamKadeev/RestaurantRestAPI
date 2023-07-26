from typing import List
import uuid
from fastapi import APIRouter, Depends, Response, status
from schema import DishCreate, DishResponse, DishBase, DishUpdate, GetDishResponse

from services.dish_service import DishService



router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Dish CRUD"]
)

@router.get(
    "/{target_menu_id}/submenus/{target_submenu_id}/dishes",
    response_model=List[DishResponse]
)
def get_dishes(service: DishService = Depends()):
    return service.get_list()


@router.get(
    "/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}",
    response_model=DishResponse
)
def get_dish(
    target_dish_id: str,
    service: DishService = Depends()
):
    print(target_dish_id)
    return service.get(target_dish_id)


@router.post(
    '/{target_menu_id}/submenus/{target_submenu_id}/dishes',
     status_code=status.HTTP_201_CREATED,
     response_model=GetDishResponse
)
def create_dish(
    target_submenu_id: str,
    dish_data: DishCreate,
    service: DishService = Depends()
):
    return service.create(target_submenu_id, dish_data)


@router.patch(
    '/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}',
    response_model=DishResponse
)
def dish_update(
    target_dish_id: str,
    update_data: DishUpdate,
    service: DishService = Depends()
):
    return service.update(target_dish_id, update_data)


@router.delete('/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}')
def delete_dish(
    target_dish_id: str,
    service: DishService = Depends()
):
    return service.delete(target_dish_id)
