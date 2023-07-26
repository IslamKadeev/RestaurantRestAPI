import uuid
from fastapi import Depends, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from typing import List

from database import get_session

from models import Dish as DishModel

from schema import DishResponse, DishBase, DishCreate, DishUpdate



class DishService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
        
    def get_list(self) -> List[DishModel]:
        dishes = (
            self.session
            .query(DishModel)
            .group_by(DishModel.id)
            .all()
        )
        
        response = []
        
        for dish in dishes:
            response.append({
                'id': dish.id,
                'title': dish.title,
                'description': dish.description,
                'price': dish.price
            })
            
        return JSONResponse(content=jsonable_encoder(response))
    
    
    def get(self, target_dish_id: str) -> DishModel:
        print(target_dish_id)
        
        dish = (
            self.session
            .query(DishModel)
            .filter_by(id=target_dish_id)
            .first()
        )
        
        if not dish:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="dish not found")
        
        # response = [{
        #     "id": dish.id,
        #     "title": dish.title,
        #     "description": dish.description,
        #     "price": str(dish.price)
        # }]
        
        # return JSONResponse(content=jsonable_encoder(response))
        return dish
    
    
    def create(self, target_submenu_id: str, dish_data: DishBase) -> DishModel:        
        new_dish = DishModel(
            title=dish_data.title,
            description=dish_data.description,
            price=dish_data.price,
            submenu_id=target_submenu_id
        )
            
        self.session.add(new_dish)
        self.session.commit()
        self.session.refresh(new_dish)
            
        return new_dish 
    
    def update(self, target_dish_id: str, update_data: DishUpdate) -> DishModel:
        dish = (
            self.session
            .query(DishModel)
            .filter(DishModel.id == target_dish_id)
        )
        
        updated_dish = dish.first()
        
        if not updated_dish:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dish not found")
        
        for field, value in update_data.model_dump(exclude_unset=True).items():
           setattr(updated_dish, field, value)
           
        self.session.commit()
        
        # response = [{
        #     "id": updated_dish.id,
        #     "title": updated_dish.title,
        #     "description": updated_dish.description,
        #     "price": updated_dish.price
        # }]
        
        # return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
        return updated_dish
    
    def delete(self, target_dish_id: str) -> DishModel:
        dish = (
            self.session
            .query(DishModel)
            .filter_by(id=target_dish_id)
            .first()
        )
        
        if not dish:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dish not found")
        
        self.session.delete(dish)
        self.session.commit()
        
        return {
            "status": True,
            "message": "The dish has been deleted"
        }
        
        
    