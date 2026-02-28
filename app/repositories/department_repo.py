from sqlalchemy.orm import Session
from app.models.department import Department


class DepartmentRepository:
    def create(self, db: Session, department: Department) -> Department:
        db.add(department)
        db.commit()
        db.refresh(department)
        return department

    def get_by_id(self, db: Session, department_id: int) -> Department | None:
        return db.query(Department).filter(Department.id == department_id).first()

    def list(self, db: Session):
        return db.query(Department).all()