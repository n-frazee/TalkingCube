from sqlalchemy import Column, Integer, String, Date, Enum

from models.base import Base

class Employee(Base):
    __tablename__ = "employees"

    emp_no = Column(Integer, primary_key=True, index=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    hire_date = Column(Date, nullable=False)

    @property
    def id(self):
        return self.emp_no

