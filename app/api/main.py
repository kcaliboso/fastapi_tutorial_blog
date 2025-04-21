from fastapi import APIRouter
from app.routers import post_router

api_router = APIRouter()

api_router.include_router(post_router.routes, prefix="/api/v1/posts", tags=['posts'])

