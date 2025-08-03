from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import uvicorn
from models import metadata

app = FastAPI()
models.Base.metadata.create_all(bind=engine) 

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/init")
def init_counter(db: db_dependency):
    counter = models.Counter(count=0)
    db.add(counter)
    db.commit()
    return counter


@app.get("/get_counter")
def get_counter(db: db_dependency):
    counter = db.query(models.Counter).first()
    if not counter:
        raise HTTPException(status_code=404, detail="Counter not found")
    return counter

@app.post("/increase_counter")
def increase_counter(db: db_dependency):
    counter = db.query(models.Counter).first()
    if not counter:
        raise HTTPException(status_code=404, detail="Counter not found")
    counter.count += 1
    db.commit()
    return counter.count


@app.post("/reset_counter")
def reset_counter(db: db_dependency):
    counter = db.query(models.Counter).first()
    if not counter:
        raise HTTPException(status_code=404, detail="Counter not found")
    counter.count = 0
    db.commit()
    return counter

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)