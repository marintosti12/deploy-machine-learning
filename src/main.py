
from fastapi import FastAPI

from config.db import SessionLocal


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
