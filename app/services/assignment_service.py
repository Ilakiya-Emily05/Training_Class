from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.assignment_repo import AssignmentRepository
from app.repositories.asset_repo import AssetRepository
from app.models.asset_assignment import AssetAssignment


class AssignmentService:
    def __init__(self):
        self.assignment_repo = AssignmentRepository()
        self.asset_repo = AssetRepository()

    def assign_asset(self, db: Session, asset_id: int, user_id: int):
        asset = self.asset_repo.get_by_id(db, asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")

        if asset.status != "AVAILABLE":
            raise HTTPException(status_code=400, detail="Asset not available")

        if self.assignment_repo.get_active_by_asset(db, asset_id):
            raise HTTPException(status_code=400, detail="Asset already assigned")

        assignment = AssetAssignment(asset_id=asset_id, user_id=user_id)
        asset.status = "ASSIGNED"

        db.add(asset)
        return self.assignment_repo.create(db, assignment)

    def return_asset(self, db: Session, asset_id: int, condition: str | None = None):
        assignment = self.assignment_repo.get_active_by_asset(db, asset_id)
        if not assignment:
            raise HTTPException(status_code=400, detail="No active assignment")

        asset = assignment.asset
        asset.status = "AVAILABLE"

        self.assignment_repo.return_asset(db, assignment, condition)
        db.add(asset)
        db.commit()

        return assignment