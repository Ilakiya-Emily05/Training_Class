from sqlalchemy.orm import Session
from app.services.leave_service import LeaveService
from app.models.leave_request import LeaveStatus

class ManagerController:

    @staticmethod
    def department_leaves(db: Session, skip: int, limit: int):
        # This assumes you add a repo function to fetch dept leaves with pagination
        return LeaveService.get_department_leaves(db, skip, limit)

    @staticmethod
    def approve_leave(db: Session, leave_id: int, status: LeaveStatus, approver_id: int):
        return LeaveService.approve_leave(db, leave_id, approver_id, status)