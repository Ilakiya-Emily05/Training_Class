from sqlalchemy.orm import Session
from app.repositories.repayment_repository import RepaymentRepository
from app.repositories.application_repository import LoanApplicationRepository
from app.schemas.repayment_schema import RepaymentCreate

class RepaymentService:
    def __init__(self, db: Session):
        self.repo = RepaymentRepository(db)
        self.application_repo = LoanApplicationRepository(db)

    def add_repayment(self, repayment_data: RepaymentCreate):
        # Optional: Check loan exists
        loan = self.application_repo.get_by_id(repayment_data.loan_application_id)
        if not loan:
            raise ValueError("Loan application not found")
        # Add repayment
        return self.repo.create(repayment_data)

    def get_repayments(self, loan_application_id: int):
        return self.repo.get_by_loan_application(loan_application_id)