from fastapi import FastAPI
from enum import Enum

class Status(str, Enum):
    draft = "draft"
    pending = "pending"
    published = "published"

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Welcome to Blog API",
    }

@app.get("/posts")
async def index():
    return {
        "message": "Posts Index",
    }

@app.get("/posts/{post_id}")
async def show(post_id: str):
    data: dict[str, str] = {
        "title": "THis is title",
        "status": Status.published,
    }
    return {
        "message": "Post Show",
        "data": data
    }

@app.post("/posts")
async def store():
    return {
        "message": "Post Create",
    }

@app.patch("/posts/{post_id}")
async def update(post_id: str):
    return {
        "message": "Post Update",
        "data": post_id
    }