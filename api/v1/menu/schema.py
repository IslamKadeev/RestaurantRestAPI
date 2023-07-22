from pydantic import BaseModel


class Menu(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True
