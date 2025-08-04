from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

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
    result : int = 0
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