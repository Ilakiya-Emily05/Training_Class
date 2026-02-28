from sqlalchemy.orm import Session
from app.services.user_service import UserService
from app.services.department_service import DepartmentService
from app.schemas.user_schema import UserCreate, UserUpdate
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate

class AdminController:

    # Users
    @staticmethod
    def list_users(db: Session, skip: int, limit: int):
        return UserService.get_all_users(db, skip, limit)

    @staticmethod
    def create_user(db: Session, data: UserCreate):
        return UserService.create_user(db, data)

    @staticmethod
    def update_user(db: Session, user_id: int, data: UserUpdate):
        return UserService.update_user(db, user_id, data)

    @staticmethod
    def delete_user(db: Session, user_id: int):
        return UserService.delete_user(db, user_id)

    # Departments
    @staticmethod
    def create_department(db: Session, data: DepartmentCreate):
        return DepartmentService.create_department(db, data)

    @staticmethod
    def update_department(db: Session, dept_id: int, data: DepartmentUpdate):
        return DepartmentService.update_department(db, dept_id, data)