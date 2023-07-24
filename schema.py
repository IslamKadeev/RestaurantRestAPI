from pydantic import BaseModel
from typing import List


class DishBase(BaseModel):
    title: str
    description: str
    price: str


class DishCreate(DishBase):
    pass


class Dish(DishBase):
    id: str

    class Config:
        orm_mode = True


class SubmenuBase(BaseModel):
    title: str
    description: str


class SubmenuCreate(SubmenuBase):
    pass


class Submenu(SubmenuBase):
    id: str
    menu_id: str
    dishes: List[Dish] = []
    dish_count: int

    class Config:
        orm_mode = True


class MenuBase(BaseModel):
    title: str
    description: str


class MenuCreate(MenuBase):
    pass


class Menu(MenuBase):
    id: str
    submenus: List[Submenu] = []
    submenu_count: int 

    class Config:
        orm_mode = True
