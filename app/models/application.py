from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func
from app.core.database import Base
import enum


class ApplicationStatus(str, enum.Enum):
    applied = "applied"
    shortlisted = "shortlisted"
    rejected = "rejected"


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    status = Column(
        Enum(ApplicationStatus),
        default=ApplicationStatus.applied,
        nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())