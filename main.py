from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chatbot

# to run: uvicorn main:app --reload

app = FastAPI()

# Enable CORS
origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot.router, tags=["Chatbot"],prefix="/chatbot")

@app.get("/")
async def root():
    return {"message": "Hello friend! -- glov_chat_backend is running."}


