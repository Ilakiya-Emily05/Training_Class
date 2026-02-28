from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    # Relationships
    users = relationship("User", back_populates="department")
    manager = relationship("User", foreign_keys=[manager_id])