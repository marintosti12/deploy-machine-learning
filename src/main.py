
from fastapi import FastAPI


from controllers.home_controller import router as ml_home_router
from controllers.predict_controller import router as predict_router


app = FastAPI()

app.include_router(ml_home_router)

app.include_router(predict_router)
