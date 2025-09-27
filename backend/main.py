# backend/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Therapist AI Platform API")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Therapist AI Platform API"}


@app.get("/api/v1/clinicians", tags=["Clinicians"])
def get_clinicians(db: Session = Depends(get_db)):
    return db.query(models.Clinician).all()
