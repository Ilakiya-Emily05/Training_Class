from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.department_repo import DepartmentRepository
from app.repositories.user_repo import UserRepository
from app.models.user import UserRole
from app.models.department import Department
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate


class DepartmentService:

    @staticmethod
    def create_department(db: Session, data: DepartmentCreate):
        if DepartmentRepository.get_by_name(db, data.name):
            raise HTTPException(400, "Department already exists")

        if data.manager_id:
            manager = UserRepository.get_by_id(db, data.manager_id)
            if not manager or manager.role != UserRole.MANAGER:
                raise HTTPException(400, "Invalid manager")

        department = Department(
            name=data.name,
            manager_id=data.manager_id
        )

        return DepartmentRepository.create(db, department)

    @staticmethod
    def update_department(db: Session, dept_id: int, data: DepartmentUpdate):
        department = DepartmentRepository.get_by_id(db, dept_id)
        if not department:
            raise HTTPException(404, "Department not found")

        if data.manager_id:
            manager = UserRepository.get_by_id(db, data.manager_id)
            if not manager or manager.role != UserRole.MANAGER:
                raise HTTPException(400, "Invalid manager")

        for field, value in data.dict(exclude_unset=True).items():
            setattr(department, field, value)

        DepartmentRepository.update(db)
        db.refresh(department)
        return department