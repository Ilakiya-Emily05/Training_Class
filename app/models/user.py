from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String(50), nullable=False)

    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)

    # Relationships
    department = relationship("Department", back_populates="users")
    assignments = relationship("AssetAssignment", back_populates="user")
    requests = relationship("AssetRequest", back_populates="employee")