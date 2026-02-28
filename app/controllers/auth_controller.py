from sqlalchemy.orm import Session
from app.services.auth_services import AuthService
from app.schemas.user_schema import UserCreate

class AuthController:

    @staticmethod
    def register(db: Session, data: UserCreate):
        return AuthService.register(db, data)

    @staticmethod
    def login(db: Session, email: str, password: str):
        return AuthService.login(db, email, password)