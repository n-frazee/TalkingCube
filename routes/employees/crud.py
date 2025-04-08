from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas
from db.db import get_db
import models.employees as models

router = APIRouter()


@router.get("/{employee_id}")
def get_employee_by_id(employee_id: int, _db: Session = Depends(get_db)):
    employees = _db.query(models.Employee).filter(models.Employee.emp_no == employee_id).first()
    return employees

@router.post("/")
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.put("/{employee_id}")
def update_employee(emp_no: int, updates: schemas.EmployeeUpdate, db: Session  = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.emp_no == emp_no).first()
    if not db_employee:
        return None

    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.delete("/{employee_id}")
def delete_employee(emp_no: int, db: Session  = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.emp_no == emp_no).first()
    if not db_employee:
        return False
    db.delete(db_employee)
    db.commit()
    return True