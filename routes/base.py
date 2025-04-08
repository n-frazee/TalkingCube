from fastapi import APIRouter

from .auth import auth
from .employees import crud


api_router = APIRouter()

api_router.include_router(crud.router, prefix="/employees", tags=["employees"])

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])