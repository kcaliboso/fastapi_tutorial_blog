from pydantic import BaseModel, Field
from app.enums.status import Status
from typing import Optional

class CommentBase(BaseModel):
    text: str = Field(..., min_length=8, max_length=255, description="Comment content")
    post_id: int = Field(..., description="ID of the post")

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int = Field(..., description="ID of the comment")

class CommentUpdate(BaseModel):
    post_id: Optional[int] = Field(None, description="ID of the post")
    text: Optional[str]= Field(None, min_length=8, max_length=255, description="Comment content")
