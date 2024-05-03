from fastapi import APIRouter,Body
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()  # .env dosyasını yükler

router = APIRouter()

apikey = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=apikey)

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-turbo"
    )


@router.get("/")
async def root():
    return {"message": "chat bot route -- glov_chat_backend is running."}

class MessageModel(BaseModel):
    role: str
    content: str
class MessagesModel(BaseModel):
    messages: List[MessageModel]


@router.post("/chat")
async def chat(messages: MessagesModel):
    print(messages)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        *messages.messages
      ]
    )
    return {"message": response.choices[0].message.content}   