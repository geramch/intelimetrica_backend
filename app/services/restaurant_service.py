from sqlalchemy import func
from sqlalchemy.orm import Session
from app.db.db import Restaurant
from app.utils.schemas import RestaurantCreate, RestaurantUpdate

class CRUDRestaurant:
    def create(self, db: Session, restaurant: RestaurantCreate) -> Restaurant:
        db_restaurant = Restaurant(**restaurant.dict())
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
        return db_restaurant.to_dict()

    def get(self, db: Session, restaurant_id: str) -> dict:
        restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
        return restaurant.to_dict() if restaurant else None

    def get_all(self, db: Session, skip: int = 0, limit: int = 10) -> list:
        return [restaurant.to_dict() for restaurant in db.query(Restaurant).offset(skip).limit(limit).all()]

    def update(self, db: Session, restaurant_id: str, restaurant: RestaurantUpdate) -> dict:
        db_restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
        if db_restaurant:
            for key, value in restaurant.dict().items():
                setattr(db_restaurant, key, value)
            db.commit()
            db.refresh(db_restaurant)
        return db_restaurant.to_dict() if db_restaurant else None

    def delete(self, db: Session, restaurant_id: str) -> dict:
        db_restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
        if db_restaurant:
            db.delete(db_restaurant)
            db.commit()
        return db_restaurant.to_dict() if db_restaurant else None

    def get_restaurants_within_radius(self, db: Session, lat: float, lng: float, radius: int) -> list:
        restaurants = db.query(Restaurant).filter(
            func.ST_Distance(
                func.ST_SetSRID(func.ST_MakePoint(Restaurant.lng, Restaurant.lat), 4326),
                func.ST_SetSRID(func.ST_MakePoint(lng, lat), 4326)
            ) <= radius
        ).all()

        count = len(restaurants)

        avg_rating = sum(restaurant.rating for restaurant in restaurants) / count if count > 0 else 0

        std_rating = (
                             sum((restaurant.rating - avg_rating) ** 2 for restaurant in restaurants) / count
                     ) ** 0.5 if count > 0 else 0

        return {
            "count": count,
            "avg": avg_rating,
            "std": std_rating
        }




crud_restaurant = CRUDRestaurant()