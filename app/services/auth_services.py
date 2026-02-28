from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User, UserRole
from app.schemas.user_schema import UserCreate


class AuthService:

    @staticmethod
    def register(db: Session, data: UserCreate):
        if UserRepository.get_by_email(db, data.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        user = User(
            name=data.name,
            email=data.email,
            password=hash_password(data.password),
            role=data.role,
            department_id=data.department_id
        )

        return UserRepository.create(db, user)

    @staticmethod
    def login(db: Session, email: str, password: str):
        user = UserRepository.get_by_email(db, email)

        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        token = create_access_token(
            data={"sub": str(user.id), "role": user.role}
        )

        return {"access_token": token, "token_type": "bearer"}