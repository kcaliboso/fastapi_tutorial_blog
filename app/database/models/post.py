from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from typing import List
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.sql import func

from app.database.config import Base
from app.enums.status import Status
from sqlalchemy.types import Enum

from app.database.models.comment import Comment


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    content = Column(Text(512))
    status = Column(Enum(Status), index=True)
    comments: Mapped[List["Comment"]] = relationship()
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
