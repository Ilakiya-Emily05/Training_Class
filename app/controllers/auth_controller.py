from sqlalchemy.orm import Session
from app.services.auth_service import AuthService


class AuthController:
    def __init__(self):
        self.service = AuthService()

    def login(self, db: Session, email: str, password: str):
        return self.service.authenticate(db, email, password)