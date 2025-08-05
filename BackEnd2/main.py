from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker
import uvicorn
from CRUD import CRUD
from db import engine

session = async_sessionmaker(bind = engine)

crud = CRUD()

app = FastAPI()

@app.post("/init")
async def init():
    result = await crud.init(session)
    return result


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
    result = await crud.get_counter(session)
    return result

@app.post('/increase')
async def increase():
    result : int = 1
    return result

@app.post('/reset')
async def reset():
    result : int = 0
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)