from pydantic import BaseModel, Field
from typing import Optional, List

class UserBase(BaseModel):
    firstname: str = Field(..., description="First name of the user")
    lastname: str = Field(..., description="Last name of the user")
    phone_number: str = Field(..., description="Phone number of the user")
    email: str = Field(..., description="Email of the user")
    password: str = Field(..., description="Password of the user")

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int = Field(..., description="ID of the user")

class UserUpdate(BaseModel):
    firstname: Optional[str] = Field(..., description="First name of the user")
    lastname: Optional[str] = Field(..., description="Last name of the user")
    phone_number: Optional[str] = Field(..., description="Phone number of the user")
    email: Optional[str] = Field(..., description="Email of the user")
    password: Optional[str] = Field(..., description="Password of the user")
