from fastapi import APIRouter
from app.routers.restaurant.endpoints import router as restaurant

api_v1_router = APIRouter()
api_v1_router.include_router(restaurant)
