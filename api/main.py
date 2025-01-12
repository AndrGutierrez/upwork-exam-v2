from fastapi import FastAPI
from users import router
from profiles import router as profile_router
from sql_app import models
from sql_app.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")
app.include_router(router, prefix='/users')
app.include_router(profile_router, prefix='/profiles')


