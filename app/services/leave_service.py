from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app.repositories.leave_repo import LeaveRepository
from app.repositories.user_repo import UserRepository
from app.models.leave_request import LeaveRequest, LeaveStatus
from app.models.user import UserRole
from app.schemas.leave_schema import LeaveCreate


class LeaveService:

    @staticmethod
    def apply_leave(db: Session, employee_id: int, data: LeaveCreate):
        if data.start_date > data.end_date:
            raise HTTPException(400, "Invalid date range")

        employee = UserRepository.get_by_id(db, employee_id)
        if not employee or employee.role != UserRole.EMPLOYEE:
            raise HTTPException(403, "Only employees can apply for leave")

        # Overlap check
        existing = LeaveRepository.get_by_employee(db, employee_id)
        for leave in existing:
            if not (data.end_date < leave.start_date or data.start_date > leave.end_date):
                raise HTTPException(400, "Overlapping leave exists")

        leave = LeaveRequest(
            employee_id=employee_id,
            start_date=data.start_date,
            end_date=data.end_date,
            reason=data.reason
        )

        return LeaveRepository.create(db, leave)

    @staticmethod
    def approve_leave(
        db: Session,
        leave_id: int,
        approver_id: int,
        status: LeaveStatus
    ):
        leave = LeaveRepository.get_by_id(db, leave_id)
        if not leave:
            raise HTTPException(404, "Leave not found")

        if leave.status != LeaveStatus.PENDING:
            raise HTTPException(400, "Leave already processed")

        approver = UserRepository.get_by_id(db, approver_id)
        employee = UserRepository.get_by_id(db, leave.employee_id)

        if approver.role == UserRole.MANAGER:
            if approver.department_id != employee.department_id:
                raise HTTPException(403, "Cannot approve outside department")

        if approver.role not in [UserRole.MANAGER, UserRole.ADMIN]:
            raise HTTPException(403, "Unauthorized")

        return LeaveRepository.update_status(
            db,
            leave,
            status=status,
            approved_by=approver_id
        )