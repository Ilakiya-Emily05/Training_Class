from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    admin = "admin"
    loan_officer = "loan_officer"
    customer = "customer"

# Base schema shared by create/update
class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole

# Schema for creating a new user
class UserCreate(UserBase):
    password: str

# Schema for updating user (password optional)
class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[UserRole]
    password: Optional[str]

# Schema for reading users from DB
class UserOut(UserBase):
    id: int

    model_config = {"from_attributes": True}  # Pydantic v2