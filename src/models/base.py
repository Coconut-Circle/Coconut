from pydantic import BaseModel

class ItemBase(BaseModel):
    id: int
    name: str

class ItemResponse(ItemBase):
    pass
