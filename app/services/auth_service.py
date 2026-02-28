from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repo import UserRepository
from app.core.security import verify_password, create_access_token


class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def authenticate(self, db: Session, email: str, password: str):
        user = self.user_repo.get_by_email(db, email)
        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        token = create_access_token(
            data={"sub": user.email, "role": user.role, "user_id": user.id}
        )
        return token