from pydantic import BaseModel


class Dish(BaseModel):
    title: str
    description: str
    price: float
    submenu_id: str

    class Config:
        orm_mode = True
