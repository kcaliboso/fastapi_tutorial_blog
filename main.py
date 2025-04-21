from fastapi import FastAPI
from app.api.main import api_router

app = FastAPI(
    title="Blog",
    description="A tutorial for FastAPI blog using pydantic model/schema for validation and SQLalchemy with MySQL for database.",
    version="1.0.0",
)

# Include the API router
app.include_router(api_router)