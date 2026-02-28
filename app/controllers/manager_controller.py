from sqlalchemy.orm import Session
from app.services.asset_service import AssetService


class ManagerController:
    def __init__(self):
        self.asset_service = AssetService()

    def list_department_assets(self, db: Session, pagination, department_id: int):
        return self.asset_service.list_assets(db, pagination, department_id=department_id)