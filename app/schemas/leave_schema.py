from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum


class LeaveStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"



class LeaveBase(BaseModel):
    start_date: date
    end_date: date
    reason: str



class LeaveCreate(LeaveBase):
    pass



class LeaveUpdate(BaseModel):
    status: LeaveStatus



class LeaveResponse(LeaveBase):
    id: int
    employee_id: int
    status: LeaveStatus
    approved_by: Optional[int]

    class Config:
        from_attributes = True