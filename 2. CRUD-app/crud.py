from sqlalchemy.orm import Session
import models, schemas


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, emp_id: int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )


def get_employee_by_email(db: Session, email: str):
    return (
        db.query(models.Employee)
        .filter(models.Employee.email == email)
        .first()
    )


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        age=employee.age
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def update_employee(
    db: Session,
    emp_id: int,
    employee: schemas.EmployeeUpdate
):
    db_employee = (
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )

    if not db_employee:
        return None

    update_data = employee.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)

    return db_employee


def delete_employee(db: Session, emp_id: int):
    db_employee = (
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )

    if not db_employee:
        return None

    db.delete(db_employee)
    db.commit()

    return db_employee