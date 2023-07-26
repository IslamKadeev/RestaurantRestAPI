from decimal import Decimal
import uuid
from pydantic import BaseModel
from typing import List


class DishBase(BaseModel):
    title: str
    description: str
    price: Decimal
    
    class Config:
        from_attributes = True


class DishCreate(DishBase):
    submenu_id: uuid.UUID | None = None
    

class DishUpdate(DishBase):
    pass


class DishResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    price: Decimal
    
    class Config:
        from_attributes = True


class GetDishResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    price: Decimal
    submenu_id: uuid.UUID | None = None
    
    class Config:
        from_attributes = True



class SubmenuResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    dishes_count: int
    
    class Config:
        from_attributes = True



class SubmenuCreate(BaseModel):
    title: str
    description: str
    #menu_id: uuid.UUID | None = None
    
    class Config:
        from_attributes = True

        

class SubmenuCreateId(SubmenuCreate):
    menu_id: str | None = None


class SubmenuUpdate(SubmenuCreate):
    pass


class MenuBase(BaseModel):
    title: str
    description: str
    
    class Config:
        from_attributes = True



class MenuCreate(MenuBase):
    pass


class MenuResponse(MenuBase):
    id: uuid.UUID


class MenuUpdate(MenuBase):
    pass


class Menu(MenuBase):
    id: str
