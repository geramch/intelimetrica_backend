from fastapi import FastAPI
from app.routers.routers import api_v1_router as routers

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(routers)