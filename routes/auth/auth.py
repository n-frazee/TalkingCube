from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db import get_db
from schemas import OAuthPayload
from models.employees import Employee

router = APIRouter()

@router.post("/")
def login_employee(payload: OAuthPayload, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.user_name == payload.user_name,
                                            Employee.password == payload.password).first()
    if db_employee is None:
        raise HTTPException(404)
    else:
        return db_employee
