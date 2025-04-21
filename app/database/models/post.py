from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from typing import List
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column
from sqlalchemy.sql import func

from app.database.config import Base
from app.enums.status import Status
from sqlalchemy.types import Enum


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    content = Column(Text(512))
    status = Column(Enum(Status), index=True)
    comments: Mapped[List["Comment"]] = relationship()
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(50), index=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
