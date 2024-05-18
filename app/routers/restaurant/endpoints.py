from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.services.restaurant_service import crud_restaurant
from app.utils.schemas import RestaurantCreate, RestaurantResponse, RestaurantUpdate
from app.db.utils import get_db
import pandas as pd
import io

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=RestaurantResponse)
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return crud_restaurant.create(db=db, restaurant=restaurant)


@router.get("/", response_model=List[RestaurantResponse])
def read_restaurants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_restaurant.get_all(db=db, skip=skip, limit=limit)


@router.get("/{restaurant_id}", response_model=RestaurantResponse)
def read_restaurant(restaurant_id: str, db: Session = Depends(get_db)):
    restaurant = crud_restaurant.get(db=db, restaurant_id=restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant


@router.put("/{restaurant_id}", response_model=RestaurantResponse)
def update_restaurant(restaurant_id: str, restaurant: RestaurantUpdate, db: Session = Depends(get_db)):
    updated_restaurant = crud_restaurant.update(db=db, restaurant_id=restaurant_id, restaurant=restaurant)
    if updated_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return updated_restaurant


@router.delete("/{restaurant_id}", response_model=RestaurantResponse)
def delete_restaurant(restaurant_id: str, db: Session = Depends(get_db)):
    deleted_restaurant = crud_restaurant.delete(db=db, restaurant_id=restaurant_id)
    if deleted_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return deleted_restaurant


@router.post("/upload_csv/")
def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = file.file.read()
    df = pd.read_csv(io.StringIO(content.decode('utf-8')))

    for _, row in df.iterrows():
        restaurant_data = row.to_dict()
        restaurant = RestaurantCreate(**restaurant_data)
        crud_restaurant.create(db=db, restaurant=restaurant)

    return {"message": "CSV data uploaded successfully"}