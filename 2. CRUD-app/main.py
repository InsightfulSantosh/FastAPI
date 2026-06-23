import models, schemas, crud

from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management System",
        "available_endpoints": [
            "GET /employees",
            "GET /employees/{emp_id}",
            "POST /employees",
            "PUT /employees/{emp_id}",
            "DELETE /employees/{emp_id}"
        ],
        "swagger_docs": "/docs",
        "redoc_docs": "/redoc"
    }

@app.post(
    "/employees",
    response_model=schemas.EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    existing_employee = crud.get_employee_by_email(db, employee.email)

    if existing_employee:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return crud.create_employee(db, employee)


@app.get("/employees", response_model=List[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@app.get("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee


@app.put("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def update_employee(
    emp_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db)
):
    db_employee = crud.update_employee(db, emp_id, employee)

    if db_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return db_employee


@app.delete("/employees/{emp_id}", response_model=dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return {"detail": "Employee Deleted"}
