# Employee Management API

A small FastAPI application that exposes CRUD endpoints for managing employee
records. The app stores records in an in-memory list, so data is reset whenever
the server restarts.

## Features

- Create employees with validation for name, department, email, age, and ID
- List all employees
- Fetch one employee by ID
- Update an employee by ID
- Delete an employee by ID
- Interactive API docs through FastAPI Swagger UI

## Requirements

- Python 3.12 or later

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Alternatively, if you use a `pyproject.toml` workflow:

```bash
pip install -e .
```

## Run The API

```bash
uvicorn main:app --reload
```

The API will be available at:

- App root: `http://127.0.0.1:8000/`
- Swagger docs: `http://127.0.0.1:8000/docs`
- ReDoc docs: `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Welcome message |
| `GET` | `/about` | API description |
| `POST` | `/add_employee` | Create an employee |
| `GET` | `/employees` | List all employees |
| `GET` | `/employee/{emp_id}` | Get one employee by ID |
| `PUT` | `/update_employee/{emp_id}` | Update one employee by ID |
| `DELETE` | `/remove_employee/{emp_id}` | Delete one employee by ID |

## Example Employee Payload

```json
{
  "id": 101,
  "name": "Santosh Kumar",
  "department": "IT",
  "email": "santosh@company.com",
  "age": 33
}
```

Allowed departments are `HR`, `IT`, `Finance`, and `Sales`.

## Example Requests

Create an employee:

```bash
curl -X POST http://127.0.0.1:8000/add_employee \
  -H "Content-Type: application/json" \
  -d '{
    "id": 101,
    "name": "Santosh Kumar",
    "department": "IT",
    "email": "santosh@company.com",
    "age": 33
  }'
```

Get all employees:

```bash
curl http://127.0.0.1:8000/employees
```

Update an employee:

```bash
curl -X PUT http://127.0.0.1:8000/update_employee/101 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Santosh Kumar",
    "department": "Finance",
    "email": "santosh@company.com",
    "age": 34
  }'
```

Delete an employee:

```bash
curl -X DELETE http://127.0.0.1:8000/remove_employee/101
```
