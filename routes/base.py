from fastapi import APIRouter
from .employees import crud


api_router = APIRouter()

api_router.include_router(crud.router, prefix="/employees", tags=["employees"])