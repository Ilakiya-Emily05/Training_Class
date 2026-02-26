from sqlalchemy.orm import Session
from app.models.repayment import Repayment
from app.schemas.repayment_schema import RepaymentCreate
from typing import List

class RepaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, repayment: RepaymentCreate) -> Repayment:
        db_repay = Repayment(**repayment.dict())
        self.db.add(db_repay)
        self.db.commit()
        self.db.refresh(db_repay)
        return db_repay

    def get_by_loan_application(self, loan_app_id: int) -> List[Repayment]:
        return self.db.query(Repayment).filter(Repayment.loan_application_id == loan_app_id).all()