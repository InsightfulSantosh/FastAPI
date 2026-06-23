from sqlalchemy import (
    Column,
    Integer,
    String,
    CheckConstraint,
    Enum,
    DateTime
)
from datetime import datetime

from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(100),
        nullable=False,
        index=True
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    age = Column(
        Integer,
        nullable=True
    )

    department = Column(
        Enum(
            "HR",
            "IT",
            "Finance",
            "Sales",
            name="department_enum"
        ),
        nullable=False,
        index=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    __table_args__ = (
        CheckConstraint(
            "age >= 1 AND age <= 120",
            name="check_age_range"
        ),
    )