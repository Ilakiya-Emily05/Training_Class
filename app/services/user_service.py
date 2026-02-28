from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.schemas.user_schema import UserUpdate


class UserService:

    @staticmethod
    def get_all_users(db: Session, skip: int, limit: int):
        return UserRepository.get_all(db, skip, limit)

    @staticmethod
    def update_user(db: Session, user_id: int, data: UserUpdate):
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        for field, value in data.dict(exclude_unset=True).items():
            setattr(user, field, value)

        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        UserRepository.delete(db, user)