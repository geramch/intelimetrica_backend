from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class RestaurantBase(BaseModel):
    rating: Optional[int] = None
    name: Optional[str] = None
    site: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(RestaurantBase):
    pass

class RestaurantResponse(RestaurantBase):
    id: str

    class Config:
        orm_mode = True
        json_encoders = {
            UUID: lambda v: str(v)  # Convert UUID to string
        }