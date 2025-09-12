from fastapi import FastAPI
from app.services import get_users, create_user
from app.schema import User

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, RUTU "}

@app.get("/users")
async def get_users_endpoint():
    return get_users()

@app.post("/users")
def add_user(user: User):
    return create_user(user)
