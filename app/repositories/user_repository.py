from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        db_user = User(
            name=user.name,
            email=user.email,
            role=user.role,
            hashed_password=user.password  # hash in service layer
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    def update_user(self, user_id: int, user_data: UserUpdate):
        db_user = self.get_user(user_id)
        if not db_user:
            return None
        for field, value in user_data.dict(exclude_unset=True).items():
            setattr(db_user, field, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.get_user(user_id)
        if not db_user:
            return None
        self.db.delete(db_user)
        self.db.commit()
        return db_user