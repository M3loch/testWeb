from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*']
)

MainCounter : int = 0

@app.get("/get_counter")
def get_counter():
    return MainCounter

@app.post("/increase_counter")
def increase_counter(newValue : int):
    global MainCounter
    MainCounter = int(newValue)
    return MainCounter
