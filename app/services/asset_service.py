from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.asset_repo import AssetRepository
from app.models.asset import Asset


class AssetService:
    def __init__(self):
        self.asset_repo = AssetRepository()

    def create_asset(self, db: Session, asset_data: dict):
        if self.asset_repo.get_by_tag(db, asset_data["asset_tag"]):
            raise HTTPException(status_code=400, detail="Asset tag already exists")

        asset = Asset(**asset_data, status="AVAILABLE")
        return self.asset_repo.create(db, asset)

    def list_assets(self, db: Session, pagination, status=None, department_id=None):
        return self.asset_repo.list(db, pagination, status, department_id)