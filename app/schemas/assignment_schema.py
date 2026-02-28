from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AssignmentCreate(BaseModel):
    asset_id: int
    user_id: int


class AssignmentResponse(BaseModel):
    id: int
    asset_id: int
    user_id: int
    assigned_date: datetime
    returned_date: Optional[datetime]
    condition_on_return: Optional[str]

    class Config:
        from_attributes = True