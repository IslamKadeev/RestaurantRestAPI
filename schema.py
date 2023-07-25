import uuid
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


class SubmenuResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    dishes_count: int
    
    class Config:
        orm_mode = True


class SubmenuCreate(BaseModel):
    title: str
    description: str
    #menu_id: uuid.UUID | None = None
    
    class Config:
        orm_mode = True
        

class SubmenuCreateId(SubmenuCreate):
    menu_id: str | None = None


class SubmenuUpdate(SubmenuCreate):
    pass


class MenuBase(BaseModel):
    title: str
    description: str
    
    class Config:
        orm_mode = True


class MenuCreate(MenuBase):
    pass


class MenuResponse(MenuBase):
    id: uuid.UUID


class MenuUpdate(MenuBase):
    pass


class Menu(MenuBase):
    id: str
