from pydantic import BaseModel, EmailStr, Field, StrictInt
from typing import Literal, Optional


class EmployeeBase(BaseModel):
    name: str = Field(
        ...,
        title="Employee Name",
        description="Full name of the employee",
        min_length=3,
        max_length=50,
        examples=["Santosh Kumar"]
    )

    department: Literal["HR", "IT", "Finance", "Sales"] = Field(
        ...,
        title="Department",
        description="Department to which the employee belongs",
        examples=["IT"]
    )

    email: EmailStr = Field(
        ...,
        title="Email Address",
        description="Official email address of the employee",
        examples=["santosh@company.com"]
    )

    age: Optional[StrictInt] = Field(
        default=None,
        title="Employee Age",
        description="Age of the employee in years",
        gt=0,
        le=120,
        examples=[33]
    )


class EmployeeCreate(EmployeeBase):
    id: int = Field(
        ...,
        title="Employee ID",
        description="Unique identifier for an employee",
        gt=0,
        examples=[101]
    )


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int = Field(
        ...,
        title="Employee ID",
        description="Unique identifier for an employee",
        examples=[101]
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 101,
                "name": "Santosh Kumar",
                "department": "IT",
                "email": "santosh@company.com",
                "age": 33
            }
        }
    }