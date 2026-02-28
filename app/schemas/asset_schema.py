from pydantic import BaseModel
from typing import Optional
from datetime import date


class AssetBase(BaseModel):
    asset_tag: str
    asset_type: str
    brand: Optional[str]
    model: Optional[str]
    purchase_date: Optional[date]
    department_id: Optional[int]


class AssetCreate(AssetBase):
    pass


class AssetResponse(AssetBase):
    id: int
    status: str

    class Config:
        from_attributes = True