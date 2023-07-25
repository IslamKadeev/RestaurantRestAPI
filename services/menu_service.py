from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session

from typing import List

from database import get_session
from models import Menu as MenuModel
from schema import Menu as MenuCreate, MenuUpdate

class MenuService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
        
    def _get(self, menu_id: str) -> MenuModel:
        menu = (
            self.session
            .query(MenuModel)
            .filter_by(id=menu_id)
            .first()
        )

        if not menu:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
        return menu
    
    def get_list(self) -> List[MenuModel]:
        menus = (
            self.session
            .query(MenuModel)
            .all()
        )
        
        return menus
    
    def get(self, menu_id: str) -> MenuModel:
        return self._get(menu_id)
    
    def create(self, creation_data: MenuCreate) -> MenuModel:
        menu = MenuModel(**creation_data.model_dump())
        self.session.add(menu)
        self.session.commit()
        
        return menu
    
    def update(self, menu_id: str, update_data: MenuUpdate) -> MenuModel:
        menu = self._get(menu_id)
        
        for field, value in update_data:
            setattr(menu, field, value)
        
        self.session.commit()
        return menu
    
    def delete(self, menu_id: str) -> MenuModel:
        menu = self._get(menu_id)
        
        self.session.delete(menu)
        self.session.commit()
        