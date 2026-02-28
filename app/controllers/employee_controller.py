from sqlalchemy.orm import Session
from app.services.request_service import RequestService


class EmployeeController:
    def __init__(self):
        self.request_service = RequestService()

    def request_asset(self, db: Session, employee_id: int, data: dict):
        return self.request_service.create_request(db, employee_id, data)