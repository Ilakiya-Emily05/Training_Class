from sqlalchemy.orm import Session
from app.services.assignment_service import AssignmentService
from app.services.request_service import RequestService


class ITAdminController:
    def __init__(self):
        self.assignment_service = AssignmentService()
        self.request_service = RequestService()

    def assign_asset(self, db: Session, asset_id: int, user_id: int):
        return self.assignment_service.assign_asset(db, asset_id, user_id)

    def approve_request(self, db: Session, request_id: int, asset_id: int, approver_id: int):
        return self.request_service.approve_request(db, request_id, asset_id, approver_id)