from sqlalchemy import Column, String, ForeignKey, Float

from api.v1 import generate_uuid
from database import Base


class Dish(Base):
    __tablename__ = 'dish'

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float(precision=2), nullable=False)
    submenu_id = Column(String, ForeignKey('submenu.id'), nullable=False, unique=True)
