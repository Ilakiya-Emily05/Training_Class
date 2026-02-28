from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.manager_controller import ManagerController
from app.dependencies.rbac import require_role
from app.database.session import get_db
from app.models.user import UserRole
from app.schemas.leave_schema import LeaveUpdate
from app.models.leave_request import LeaveStatus

router = APIRouter(prefix="/manager", tags=["Manager"], dependencies=[Depends(require_role(UserRole.MANAGER))])

@router.get("/leaves")
def department_leaves(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return ManagerController.department_leaves(db, skip, limit)

@router.patch("/leaves/{leave_id}")
def approve_leave(leave_id: int, status: LeaveStatus, db: Session = Depends(get_db)):
    return ManagerController.approve_leave(db, leave_id, status)