from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    EMPLOYEE = "EMPLOYEE"



class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole
    department_id: Optional[int] = None



class UserCreate(UserBase):
    password: str



class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[UserRole] = None
    department_id: Optional[int] = None



class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True