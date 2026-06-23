from pydantic import BaseModel, Field, EmailStr, StrictInt
from typing import Optional, Literal


class EmployeeBase(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Employee full name"
    )

    email: EmailStr = Field(
        ...,
        description="Unique employee email address"
    )

    department: Literal[
        "HR",
        "IT",
        "Finance",
        "Sales"
    ] = Field(
        ...,
        description="Employee department"
    )

    age: Optional[StrictInt] = Field(
        default=None,
        ge=1,
        le=120,
        description="Employee age must be between 1 and 120"
    )


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=100,
        description="Employee full name"
    )

    email: Optional[EmailStr] = Field(
        default=None,
        description="Unique employee email address"
    )

    department: Optional[
        Literal[
            "HR",
            "IT",
            "Finance",
            "Sales"
        ]
    ] = Field(
        default=None,
        description="Employee department"
    )

    age: Optional[StrictInt] = Field(
        default=None,
        ge=1,
        le=120,
        description="Employee age must be between 1 and 120"
    )


class EmployeeResponse(EmployeeBase):
    id: int

    model_config = {
        "from_attributes": True
    }