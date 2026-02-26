from pydantic import BaseModel
from typing import Optional

class LoanProductBase(BaseModel):
    product_name: str
    interest_rate: float
    max_amount: float
    tenure_months: int
    description: Optional[str]

class LoanProductCreate(LoanProductBase):
    pass

class LoanProductUpdate(BaseModel):
    product_name: Optional[str]
    interest_rate: Optional[float]
    max_amount: Optional[float]
    tenure_months: Optional[int]
    description: Optional[str]

class LoanProductOut(LoanProductBase):
    id: int

    model_config = {"from_attributes": True}