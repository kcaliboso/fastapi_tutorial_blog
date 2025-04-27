from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(255), index=True)
    lastname = Column(String(255), index=True)
    phone_number = Column(String(255), index=True)
    email = Column(String(255), index=True)
    password = Column(String(255), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
