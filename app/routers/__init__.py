from fastapi import APIRouter
from .auth import auth_router

main_router = APIRouter()
main_router.include_router(auth_router)