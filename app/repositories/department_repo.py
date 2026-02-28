from sqlalchemy.orm import Session
from app.models.department import Department


class DepartmentRepository:

    @staticmethod
    def create(db: Session, department: Department):
        db.add(department)
        db.commit()
        db.refresh(department)
        return department

    @staticmethod
    def get_by_id(db: Session, dept_id: int):
        return db.query(Department).filter(Department.id == dept_id).first()

    @staticmethod
    def get_by_name(db: Session, name: str):
        return db.query(Department).filter(Department.name == name).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Department).offset(skip).limit(limit).all()

    @staticmethod
    def update(db: Session):
        db.commit()

    @staticmethod
    def delete(db: Session, department: Department):
        db.delete(department)
        db.commit()