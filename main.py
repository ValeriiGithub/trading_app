# uvicorn main:app --reload
# http://127.0.0.1:8000/docs - обращение через swagger
# http://127.0.0.1:8000/redoc - менее удобный

from fastapi import FastAPI
from fastapi_users import fastapi_users

from auth.auth import auth_backend

app = FastAPI(
    title="Trading App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)