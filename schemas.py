from typing import Optional

from pydantic import BaseModel
from datetime import date

class EmployeeUpdate(BaseModel):
    birth_date: Optional[date] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    hire_date: Optional[date] = None
    password: Optional[str] = None
    user_name: Optional[str] = None

class EmployeeCreate(EmployeeUpdate):
    emp_no: int


class Employee(BaseModel):
    emp_no: int
    birth_date: date
    first_name: str
    last_name: str
    gender: str
    hire_date: date
    password: str
    user_name: str

    class Config:
        orm_mode = True

class OAuthPayload(BaseModel):
    user_name: str
    password: str

class OAuthResponse(BaseModel):
    access_token: str

