from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from database import engine
from sqlalchemy.orm import Session
import uvicorn
from database import metadata

app = FastAPI()
metadata.create_all(engine) 


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)