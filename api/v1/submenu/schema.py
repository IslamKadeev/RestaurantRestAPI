from pydantic import BaseModel


class Submenu(BaseModel):
    title: str
    description: str
    menu_id: str

    class Config:
        orm_mode = True
