from fastapi import APIRouter
from src.models.base import ItemBase, ItemResponse

router = APIRouter()

# Endpoint to get user details
@router.get("/{id}", response_model=ItemResponse)
async def get_user(id: int):
    return {"id": id, "name": f"User {id}"}

# Endpoint to create a new user (for demonstration)
@router.post("/", response_model=ItemResponse)
async def create_user(user: ItemBase):
    return {"id": user.id, "name": user.name}
