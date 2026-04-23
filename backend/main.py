from fastapi import FastAPI
from pydantic import BaseModel
#from database import collection

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "FastAPI backend is running"}