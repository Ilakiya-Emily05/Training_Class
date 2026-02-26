from sqlalchemy import Column, Integer, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum
from datetime import datetime

class PaymentStatus(str, enum.Enum):
    completed = "completed"
    pending = "pending"

class Repayment(Base):
    __tablename__ = "repayments"

    id = Column(Integer, primary_key=True, index=True)
    loan_application_id = Column(Integer, ForeignKey("loan_applications.id"), nullable=False)
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.pending)

    # Relationships
    loan_application = relationship("LoanApplication", back_populates="repayments")