from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    admin = "admin"
    recruiter = "recruiter"
    candidate = "candidate"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[UserRole]
    password: Optional[str]

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True 