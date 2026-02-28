from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.request_repo import RequestRepository
from app.services.assignment_service import AssignmentService
from app.models.asset_request import AssetRequest


class RequestService:
    def __init__(self):
        self.request_repo = RequestRepository()
        self.assignment_service = AssignmentService()

    def create_request(self, db: Session, employee_id: int, data: dict):
        request = AssetRequest(
            employee_id=employee_id,
            asset_type=data["asset_type"],
            reason=data.get("reason"),
            status="PENDING"
        )
        return self.request_repo.create(db, request)

    def approve_request(self, db: Session, request_id: int, asset_id: int, approver_id: int):
        request = self.request_repo.get_by_id(db, request_id)
        if not request or request.status != "PENDING":
            raise HTTPException(status_code=400, detail="Invalid request")

        self.assignment_service.assign_asset(
            db=db,
            asset_id=asset_id,
            user_id=request.employee_id
        )

        request.status = "APPROVED"
        request.approved_by = approver_id

        return self.request_repo.update(db, request)

    def reject_request(self, db: Session, request_id: int, approver_id: int):
        request = self.request_repo.get_by_id(db, request_id)
        if not request or request.status != "PENDING":
            raise HTTPException(status_code=400, detail="Invalid request")

        request.status = "REJECTED"
        request.approved_by = approver_id

        return self.request_repo.update(db, request)