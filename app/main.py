from fastapi import FastAPI
from .database import engine
from .models import Base
from . import routers

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(routers.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the DIREMAS: Digital Receipts Management System !"}
