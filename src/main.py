
from fastapi import FastAPI, Depends, HTTPException
import pandas as pd
from contextlib import asynccontextmanager

from config.db import SessionLocal
from schemas.ModelFeatures import ModelFeatures
from model_loader import load_model 
from features import compute_features

from sqlalchemy.orm import Session

from controllers.home_controller import router as ml_home_router
from controllers.predict_controller import router as predict_router

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

app = FastAPI()

app.include_router(ml_home_router)

app.include_router(predict_router)
