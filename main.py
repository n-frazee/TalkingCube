
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas
from db.db import get_db
from routes.base import api_router
from routes.employees import crud
app = FastAPI()

app.include_router(api_router, prefix="/api")


