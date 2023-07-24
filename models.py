from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


def generate_uuid():
    return str(uuid4())


Base = declarative_base()


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


class Submenu(Base):
    __tablename__ = "submenu"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    menu_id = Column(String, ForeignKey('menu.id'), nullable=False)

    dishes = relationship('Dish', backref='submenu', cascade='all, delete-orphan')

    def get_dish_count(self):
        return len(self.dishes)


class Dish(Base):
    __tablename__ = 'dish'

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric(precision=4, scale=2), nullable=False)
    submenu_id = Column(String, ForeignKey('submenu.id'), nullable=False)
