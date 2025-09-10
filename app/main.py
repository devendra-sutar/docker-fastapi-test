from fastapi import FastAPI
from .services import get_users, create_user
from .schema import User

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Docker FastAPI!"}

@app.get("/users")
def read_users():
    return get_users()

@app.post("/users")
def add_user(user: User):
    return create_user(user)
