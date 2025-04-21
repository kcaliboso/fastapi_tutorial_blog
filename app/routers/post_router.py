from fastapi import APIRouter, HTTPException, status, Depends
from app.database.schemas.post import Post, PostCreate, PostUpdate
from app.response.api_response import APIResponse
from app.controllers import post_controller
from sqlalchemy.orm import Session
from app.database.config import get_db

routes = APIRouter()


# Get all posts
@routes.get("/", response_model=APIResponse[Post])
def index(db: Session = Depends(get_db), limit: int = 10):
    db_posts = post_controller.get_posts(db=db, limit=limit)
    return APIResponse(status="success", status_code=status.HTTP_200_OK, message="Post List", data=db_posts)


# Get a post with post_id
@routes.get("/{post_id}", response_model=APIResponse[Post])
def show(post_id: int, db: Session = Depends(get_db)):
    db_post = post_controller.get_post(db=db, post_id=post_id)

    if db_post:
        return APIResponse(status="success", status_code=status.HTTP_200_OK, message="Post Details", data=db_post)

    raise HTTPException(status_code=404, detail="Post not found")


# Create a post
@routes.post("/", response_model=APIResponse[Post])
def store(post: PostCreate, db: Session = Depends(get_db)):
    new_post = post_controller.create_post(db=db, post=post)
    return APIResponse(status="success", status_code=status.HTTP_200_OK, message="Post created", data=new_post)


# Update post
@routes.patch("/{post_id}", response_model=APIResponse[Post])
def update(post_id: int, updated_post: PostUpdate, db: Session = Depends(get_db)):
    db_post = post_controller.update_post(db=db, post_id=post_id, updated_post=updated_post)

    if not db_post:
        raise HTTPException(404, detail="Post not found")

    return APIResponse(status="success", status_code=status.HTTP_200_OK, message="Post updated", data=db_post)


# Delete post
@routes.delete("/{post_id}", response_model=APIResponse)
def destroy(post_id: int, db: Session = Depends(get_db)):
    db_post = post_controller.delete_post(db=db, post_id=post_id)

    if not db_post:
        raise HTTPException(404, detail="Post not found")

    return APIResponse(status="success", status_code=status.HTTP_200_OK, message="Post deleted.")
