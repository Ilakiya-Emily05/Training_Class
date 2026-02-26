from pydantic import BaseModel
from datetime import datetime


class ApplicationCreate(BaseModel):
    user_id: int
    job_id: int


class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    job_id: int
    created_at: datetime

    class Config:
        from_attributes = True   