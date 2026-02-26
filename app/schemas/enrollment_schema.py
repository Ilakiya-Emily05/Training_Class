from pydantic import BaseModel, Field

# Request model for enrolling a student
class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

# Response model for returning enrollment info
class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int

    class Config:
        orm_mode = True