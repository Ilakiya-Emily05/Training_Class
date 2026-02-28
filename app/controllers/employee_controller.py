from sqlalchemy.orm import Session
from app.services.leave_service import LeaveService
from app.schemas.leave_schema import LeaveCreate

class EmployeeController:

    @staticmethod
    def apply_leave(db: Session, employee_id: int, data: LeaveCreate):
        return LeaveService.apply_leave(db, employee_id, data)

    @staticmethod
    def my_leaves(db: Session, employee_id: int):
        return LeaveService.get_employee_leaves(db, employee_id)