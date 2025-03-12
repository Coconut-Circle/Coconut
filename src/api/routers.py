from fastapi import APIRouter
from .login import router as login_router
from .users import router as users_router

api_router = APIRouter()

# Include routers for each set of endpoints
api_router.include_router(login_router, prefix="", tags=["Login"])
api_router.include_router(users_router, prefix="", tags=["Users"])
