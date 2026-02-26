from sqlalchemy.orm import Session
from app.repositories.application_repository import LoanApplicationRepository
from app.repositories.product_repository import LoanProductRepository
from app.schemas.application_schema import LoanApplicationCreate, LoanApplicationUpdateStatus
from app.models.user import UserRole

class ApplicationService:
    def __init__(self, db: Session):
        self.repo = LoanApplicationRepository(db)
        self.product_repo = LoanProductRepository(db)

    def create_application(self, application_data: LoanApplicationCreate):
        # Check requested_amount <= product.max_amount
        product = self.product_repo.get_by_id(application_data.product_id)
        if not product:
            raise ValueError("Loan product not found")
        if application_data.requested_amount > product.max_amount:
            raise ValueError("Requested amount exceeds max loan amount")
        return self.repo.create(application_data)

    def get_application(self, application_id: int):
        return self.repo.get_by_id(application_id)

    def list_applications(self, skip: int = 0, limit: int = 100):
        return self.repo.get_all(skip=skip, limit=limit)

    def update_status(self, application_id: int, status_update: LoanApplicationUpdateStatus, user_role: str):
        # Only loan_officer can approve/reject
        if status_update.status in ["approved", "rejected"] and user_role != UserRole.loan_officer:
            raise PermissionError("Only loan officer can approve/reject")
        return self.repo.update_status(application_id, status_update)