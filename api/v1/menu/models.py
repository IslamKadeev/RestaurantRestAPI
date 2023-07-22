from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from uuid import uuid4

from database import Base


class Menu(Base):
    __tablename__ = "menu"
