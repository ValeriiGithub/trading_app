# uvicorn main:app --reload
# http://127.0.0.1:8000/docs - обращение через swagger
# http://127.0.0.1:8000/redoc - менее удобный

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_hello():
    return "Hello world"
