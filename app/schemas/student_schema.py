from pydantic import BaseModel, EmailStr, Field

# Request model for creating a student
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr

# Response model for returning student details
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True