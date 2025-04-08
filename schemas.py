from typing import Optional

from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):
    emp_no: int
    birth_date: date
    first_name: str
    last_name: str
    gender: str
    hire_date: date

class Employee(BaseModel):
    emp_no: int
    birth_date: date
    first_name: str
    last_name: str
    gender: str
    hire_date: date

    class Config:
        orm_mode = True

class EmployeeUpdate(BaseModel):
    birth_date: Optional[date] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    hire_date: Optional[date] = None

