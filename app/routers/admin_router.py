from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.admin_controller import AdminController
from app.dependencies.rbac import require_role
from app.database.session import get_db
from app.schemas.user_schema import UserCreate, UserUpdate
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate
from app.models.user import UserRole

router = APIRouter(prefix="/admin", tags=["Admin"], dependencies=[Depends(require_role(UserRole.ADMIN))])

# Users
@router.get("/users")
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return AdminController.list_users(db, skip, limit)

@router.post("/users")
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return AdminController.create_user(db, data)

@router.patch("/users/{user_id}")
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return AdminController.update_user(db, user_id, data)

# Departments
@router.post("/departments")
def create_department(data: DepartmentCreate, db: Session = Depends(get_db)):
    return AdminController.create_department(db, data)

@router.patch("/departments/{dept_id}")
def update_department(dept_id: int, data: DepartmentUpdate, db: Session = Depends(get_db)):
    return AdminController.update_department(db, dept_id, data)