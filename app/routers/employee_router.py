from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.employee_controller import EmployeeController
from app.dependencies.rbac import require_role
from app.database.session import get_db
from app.schemas.leave_schema import LeaveCreate
from app.models.user import UserRole

router = APIRouter(prefix="/employee", tags=["Employee"], dependencies=[Depends(require_role(UserRole.EMPLOYEE))])

@router.post("/leaves")
def apply_leave(data: LeaveCreate, db: Session = Depends(get_db)):
    return EmployeeController.apply_leave(db, data)

@router.get("/leaves")
def my_leaves(db: Session = Depends(get_db)):
    return EmployeeController.my_leaves(db)