from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from CRUD import CRUD
from db import engine


crud = CRUD()

app = FastAPI()

@app.post("/init")
async def init():
    pass


@app.get("/")
async def welcome():
    return {
            "welcome":"/",
            "get":"/get",
            "increase":"/increase",
            "reset":"/reset"
            }

@app.get("/get")
async def get():
    pass

@app.post('/increase')
async def increase():
    pass

@app.post('/reset')
async def reset():
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)