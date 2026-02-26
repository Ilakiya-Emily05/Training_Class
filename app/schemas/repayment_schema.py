from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum

class PaymentStatus(str, Enum):
    completed = "completed"
    pending = "pending"

class RepaymentBase(BaseModel):
    loan_application_id: int
    amount_paid: float
    payment_date: date
    payment_status: PaymentStatus

class RepaymentCreate(RepaymentBase):
    pass

class RepaymentOut(RepaymentBase):
    id: int

    model_config = {"from_attributes": True}