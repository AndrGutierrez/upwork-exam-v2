from fastapi import FastAPI
from users import router
from sql_app import models
from sql_app.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router, prefix='/users')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
