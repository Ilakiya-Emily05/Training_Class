from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class UserRole(str, enum.Enum):
    admin = "admin"
    loan_officer = "loan_officer"
    customer = "customer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    hashed_password = Column(String, nullable=False)

    # Relationships
    loan_applications = relationship("LoanApplication", back_populates="customer", foreign_keys="LoanApplication.user_id")
    processed_applications = relationship("LoanApplication", back_populates="loan_officer", foreign_keys="LoanApplication.processed_by")