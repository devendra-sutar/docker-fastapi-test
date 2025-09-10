import json
from .schema import User

DATA_FILE = './app/data/users.json'

def load_users():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def get_users():
    return load_users()

def create_user(user: User):
    users = load_users()
    users.append(user.dict())
    save_users(users)
    return user
