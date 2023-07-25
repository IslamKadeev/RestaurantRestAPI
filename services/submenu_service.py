import uuid
from fastapi import Depends, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from typing import List

from database import get_session
from models import Submenu as SubmenuModel
from models import Menu as MenuModel
from models import Dish as DishModel
from schema import SubmenuCreate, SubmenuUpdate, SubmenuCreateId


class SubmenuService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    
    def get_list(self) -> List[SubmenuModel]:
        submenus = (
            self.session
            .query(SubmenuModel)
            .group_by(SubmenuModel.id)
            .all()
        )

        submenus_response = []
        
        for submenu in submenus:
            submenus_response.append({
                "id": submenu.id,
                "title": submenu.title,
                "description": submenu.description,
                "dishes_count": submenu.get_dish_count()
            })
        
        return submenus_response
    
    def get(self, target_submenu_id: str) -> SubmenuModel:
        submenu = (
            self.session
            .query(SubmenuModel)
            .filter_by(id=target_submenu_id)
            .first()
        )
        
        if not submenu:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="submenu not found")
        
        
        submenu_response = {
            'id': submenu.id,
            'title': submenu.title,
            'description': submenu.description,
            'dishes_count': submenu.get_dish_count()
        }
        
        return JSONResponse(content=jsonable_encoder(submenu_response))
    
    
    def create(
        self,
        target_menu_id: str,
        submenu_data: SubmenuCreate
    ) -> SubmenuModel:
        
        submenu = SubmenuCreateId(
            title=submenu_data.title,
            description=submenu_data.description,
            menu_id=target_menu_id
        )
        
        new_submenu = SubmenuModel(**submenu.model_dump())
        
        self.session.add(new_submenu)
        self.session.commit()
        self.session.refresh(new_submenu)
        
        response = {
            "id": new_submenu.id,
            "title": new_submenu.title,
            "description": new_submenu.description,
            "dishes_count": new_submenu.get_dish_count()
        }
        
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)    
    
    def update(self, target_submenu_id: str, update_data: SubmenuUpdate) -> SubmenuModel:
        submenu = (
            self.session
            .query(SubmenuModel)
            .filter(SubmenuModel.id == target_submenu_id)
        )

        updated_submenu = submenu.first()

        if not updated_submenu:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Submenu not found")

        for field, value in update_data.model_dump(exclude_unset=True).items():
           setattr(updated_submenu, field, value)

        self.session.commit()
        
        response = {
            "id": updated_submenu.id,
            "title": updated_submenu.title,
            "description": updated_submenu.description,
            "dishes_count": updated_submenu.get_dish_count()
        }
        
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    
    
    def delete(self, target_submenu_id: str) -> SubmenuModel:
        submenu = (
            self.session
            .query(SubmenuModel)
            .filter_by(id=target_submenu_id)
            .first()
        )
        
        if not submenu:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="submenu not found")
            
        self.session.delete(submenu)
        self.session.commit()
        
        return {
            "status": True,
            "message": "The submenu has been deleted"
        }