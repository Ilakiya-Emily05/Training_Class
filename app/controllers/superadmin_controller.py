from sqlalchemy.orm import Session
from app.services.asset_service import AssetService


class SuperAdminController:
    def __init__(self):
        self.asset_service = AssetService()

    def create_asset(self, db: Session, data: dict):
        return self.asset_service.create_asset(db, data)