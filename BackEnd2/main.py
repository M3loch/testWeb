from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from CRUD import CRUD
from db import engine
from schemas import TestPostDTO, TestGetDTO
import asyncio



crud = CRUD()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/get")
async def get():
    res = await CRUD.get_all()
    return res

@app.get('/get_by_id/{id}')
async def get_by_id(id):
    try:
        res = await CRUD.get_by_id(int(id))
        return res
    except Exception as e:
        print(f"{e}")

@app.post('/add')
async def add(newValue: TestPostDTO):
    try:
        res = await CRUD.add(newValue.value)
        return res
    except Exception as e:
        print(f"{e}")


@app.put('/update')
async def update(newValue: TestGetDTO):
     res = await CRUD.set_value(newValue.id, newValue.value)
     return res 

@app.delete('/delete/{id}')
async def delete(id : int):
    res = await CRUD.delete(id)
    return res

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)