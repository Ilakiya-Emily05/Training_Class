from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def list(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    def create(self, user: UserCreate):
        db_user = User(
            name=user.name,
            email=user.email,
            role=user.role,
            hashed_password=user.password  # hash later in service
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, db_user: User, user_update: UserUpdate):
        for field, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, field, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, db_user: User):
        self.db.delete(db_user)
        self.db.commit()