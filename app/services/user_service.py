from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, user: UserCreate):
        return self.repo.create(user)