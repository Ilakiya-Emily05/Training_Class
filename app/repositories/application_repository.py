from sqlalchemy.orm import Session
from app.models.loan_application import LoanApplication
from app.schemas.application_schema import LoanApplicationCreate, LoanApplicationUpdateStatus
from typing import List, Optional

class LoanApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, application: LoanApplicationCreate) -> LoanApplication:
        db_app = LoanApplication(**application.dict())
        self.db.add(db_app)
        self.db.commit()
        self.db.refresh(db_app)
        return db_app

    def get_by_id(self, application_id: int) -> Optional[LoanApplication]:
        return self.db.query(LoanApplication).filter(LoanApplication.id == application_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[LoanApplication]:
        return self.db.query(LoanApplication).offset(skip).limit(limit).all()

    def update_status(self, application_id: int, status_update: LoanApplicationUpdateStatus) -> Optional[LoanApplication]:
        db_app = self.get_by_id(application_id)
        if not db_app:
            return None
        for field, value in status_update.dict(exclude_unset=True).items():
            setattr(db_app, field, value)
        self.db.commit()
        self.db.refresh(db_app)
        return db_app