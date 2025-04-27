from pydantic import BaseModel, Field
from app.database.schemas.comment import Comment
from app.enums.status import Status
from typing import Optional, List

class PostBase(BaseModel):
    title: str = Field(..., min_length=8, max_length=128, description="Title of the post")
    content: str = Field(..., min_length=1, max_length=1048, description="Post content")
    status: Status = Field(default=Status.Draft, description="Post status")
    comments: List[Comment] = []

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int = Field(..., description="ID of the post")

class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=8, max_length=128, description="Title of the post")
    content: Optional[str] = Field(None, min_length=1, max_length=1048, description="Post content")
    status: Optional[Status] = Field(None, description="Post status")
