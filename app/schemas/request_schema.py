from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AssetRequestCreate(BaseModel):
    asset_type: str
    reason: Optional[str]


class AssetRequestResponse(BaseModel):
    id: int
    employee_id: int
    asset_type: str
    reason: Optional[str]
    status: str
    approved_by: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True