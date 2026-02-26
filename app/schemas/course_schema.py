from pydantic import BaseModel, Field

# Request model for creating a course
class CourseCreate(BaseModel):
    title: str = Field(..., min_length=1)
    duration: int = Field(..., gt=0, description="Duration in hours")

# Response model for returning course details
class CourseResponse(BaseModel):
    id: int
    title: str
    duration: int

    class Config:
        orm_mode = True