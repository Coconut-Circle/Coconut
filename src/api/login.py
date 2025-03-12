from fastapi import APIRouter
from src.models.base import ItemResponse

router = APIRouter()

@router.get("/", response_model=ItemResponse)
async def get_login():
    return {"id": 1, "name": "Hello! Welcome to the Coconut Backend!"}
