from sqlalchemy.orm import Session
from app.models.leave_request import LeaveRequest, LeaveStatus


class LeaveRepository:

    @staticmethod
    def create(db: Session, leave: LeaveRequest):
        db.add(leave)
        db.commit()
        db.refresh(leave)
        return leave

    @staticmethod
    def get_by_id(db: Session, leave_id: int):
        return db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()

    @staticmethod
    def get_by_employee(db: Session, employee_id: int):
        return (
            db.query(LeaveRequest)
            .filter(LeaveRequest.employee_id == employee_id)
            .all()
        )

    @staticmethod
    def get_department_leaves(db: Session, department_id: int):
        return (
            db.query(LeaveRequest)
            .join(LeaveRequest.employee)
            .filter_by(department_id=department_id)
            .all()
        )

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10):
        return (
            db.query(LeaveRequest)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def update_status(db: Session, leave: LeaveRequest, status: LeaveStatus, approved_by: int | None):
        leave.status = status
        leave.approved_by = approved_by
        db.commit()
        db.refresh(leave)
        return leave