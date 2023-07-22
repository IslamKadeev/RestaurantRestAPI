from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from api.v1 import generate_uuid
from database import Base


class Menu(Base):
    __tablename__ = "menu"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    submenus = relationship('Submenu', backref='menu', cascade='all, delete-orphan')

    def get_submenu_count(self):
        return len(self.submenus)

    def get_total_dish_count(self):
        total_dish_count = 0
        for submenu in self.submenus:
            total_dish_count += submenu.get_dish_count()
        return total_dish_count
