from pydantic import BaseModel
from typing import Optional

class JobBase(BaseModel):
    title: str
    description: str
    salary: float
    company_id: int  

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    salary: Optional[float]
    company_id: Optional[int]

class JobResponse(JobBase):
    id: int

    class Config:
        from_attributes = True