from sqlalchemy import Column, Integer, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class ApplicationStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    disbursed = "disbursed"
    closed = "closed"

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("loan_products.id"), nullable=False)
    requested_amount = Column(Float, nullable=False)
    approved_amount = Column(Float)
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.pending)
    processed_by = Column(Integer, ForeignKey("users.id"))

    # Relationships
    customer = relationship("User", back_populates="loan_applications", foreign_keys=[user_id])
    loan_officer = relationship("User", back_populates="processed_applications", foreign_keys=[processed_by])
    loan_product = relationship("LoanProduct", back_populates="applications")
    repayments = relationship("Repayment", back_populates="loan_application")