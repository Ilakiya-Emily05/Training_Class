from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.schemas.user_schema import UserRole

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    role = Column(Enum(UserRole), nullable=False)
    hashed_password = Column(String, nullable=False)

    applications = relationship("Application", back_populates="user")