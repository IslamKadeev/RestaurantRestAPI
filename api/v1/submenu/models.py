from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from api.v1 import generate_uuid
from database import Base


class Submenu(Base):
    __tablename__ = "submenu"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    menu_id = Column(String, ForeignKey('menu.id'), nullable=False, unique=True)

    dishes = relationship('Dish', backref='submenu', cascade='all, delete-orphan')

    def get_dish_count(self):
        return len(self.dishes)
