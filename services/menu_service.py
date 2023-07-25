from fastapi import Depends, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

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
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="menu not found"
            )
        
        return menu
    
    def get_list(self) -> List[MenuModel]:
        menus = (
            self.session
            .query(MenuModel)
            .all()
        )
        
        return menus
    
    def get(self, menu_id: str) -> MenuModel:
        menu = self._get(menu_id)
        
        submenus = menu.get_submenu_count()
        dishes_count = menu.get_total_dish_count()
        
        menu_response = {
            'id': menu_id,
            'title': menu.title,
            'description': menu.description,
            'submenus_count': submenus,
            'dishes_count': dishes_count
        }
        
        return JSONResponse(content=jsonable_encoder(menu_response))
    
    def create(self, creation_data: MenuCreate) -> MenuModel:
        menu = MenuModel(**creation_data.model_dump())
        self.session.add(menu)
        self.session.commit()
        
        return menu
    
    def update(self, menu_id: str, update_data: MenuUpdate) -> MenuModel:
        menu = self._get(menu_id)
        
        if not menu:
            raise HTTPException(status_code=status.HTTP_200_OK)
        
        for field, value in update_data:
            setattr(menu, field, value)
        
        self.session.commit()
        
        return menu
    
    def delete(self, menu_id: str) -> MenuModel:
        menu = self._get(menu_id)
        
        print(menu_id)
        print(menu)
        
        if not menu:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
        self.session.delete(menu)
        self.session.commit()