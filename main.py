from fastapi import FastAPI, HTTPException
from typing import List

from model import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)

app = FastAPI(
    title="Employee Management API",
    description="CRUD operations for Employee Management",
    version="1.0.0"
)

employees_db: List[EmployeeResponse] = []


@app.get("/")
def home():
    return {"message": "Welcome to Employee Dashboard"}


@app.get("/about")
def about():
    return {
        "message": "This website is designed for doing CRUD operations over employee data"
    }


@app.post(
    "/add_employee",
    response_model=EmployeeResponse,
    summary="Create Employee",
    description="Add a new employee to the system"
)
def add_employee(new_employee: EmployeeCreate):

    for employee in employees_db:
        if employee.id == new_employee.id:
            raise HTTPException(
                status_code=400,
                detail=f"Employee with EmployeeID {new_employee.id} already exists"
            )

    employee = EmployeeResponse(**new_employee.model_dump())

    employees_db.append(employee)

    return employee


@app.get(
    "/employees",
    response_model=List[EmployeeResponse],
    summary="Get All Employees"
)
def get_employees():
    return employees_db


@app.get(
    "/employee/{emp_id}",
    response_model=EmployeeResponse,
    summary="Get Employee By ID"
)
def get_employee(emp_id: int):

    for employee in employees_db:
        if employee.id == emp_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


@app.put(
    "/update_employee/{emp_id}",
    response_model=EmployeeResponse,
    summary="Update Employee"
)
def update_employee(
    emp_id: int,
    updated_employee: EmployeeUpdate
):

    for index, employee in enumerate(employees_db):

        if employee.id == emp_id:

            employees_db[index] = EmployeeResponse(
                id=emp_id,
                **updated_employee.model_dump()
            )

            return employees_db[index]

    raise HTTPException(
        status_code=404,
        detail=f"Employee with EmployeeID {emp_id} not found"
    )


@app.delete(
    "/remove_employee/{emp_id}",
    summary="Delete Employee"
)
def remove_employee(emp_id: int):

    for index, employee in enumerate(employees_db):

        if employee.id == emp_id:

            employees_db.pop(index)

            return {
                "message": f"Employee with EmployeeID {emp_id} successfully removed"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )