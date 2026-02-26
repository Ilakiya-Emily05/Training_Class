from pydantic import BaseModel
from typing import Optional
from enum import Enum

class LoanStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    disbursed = "disbursed"
    closed = "closed"

class LoanApplicationBase(BaseModel):
    user_id: int
    product_id: int
    requested_amount: float

class LoanApplicationCreate(LoanApplicationBase):
    pass

class LoanApplicationUpdateStatus(BaseModel):
    status: LoanStatus
    approved_amount: Optional[float]
    processed_by: Optional[int]

class LoanApplicationOut(LoanApplicationBase):
    id: int
    approved_amount: Optional[float]
    status: LoanStatus
    processed_by: Optional[int]

    model_config = {"from_attributes": True}