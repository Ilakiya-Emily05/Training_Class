from app.models.user import User
from app.core.database import SessionLocal

class UserService:
    def __init__(self):
        self.db = SessionLocal()

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user