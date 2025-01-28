from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from constants import SERVER_URL,PORT,ENV
from pydantic import BaseModel
import os
from google import genai

app = FastAPI()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

@asynccontextmanager
async def lifespan(app:FastAPI):
    yield
    
app=FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"server is running good"}

class GenerateRequest(BaseModel):
    content: str

class GenerateResponse(BaseModel):
    text: str

@app.post("/generate", response_model=GenerateResponse)
async def generate_content(request: GenerateRequest):
    """
    Generate content using Google GenAI's gemini-2.0-flash-exp model.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=request.content
        )
        return GenerateResponse(text=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=SERVER_URL, port=int(PORT),reload=(ENV=="dev"))
