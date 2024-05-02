from fastapi import APIRouter,Body
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "chat bot route -- glov_chat_backend is running."}

class Item(BaseModel):
    message: str


@router.post("/chat")
async def chat(item:Item):
    print(item.message)
    return {"message": "chat bot route -- glov_chat_backend is running."}   