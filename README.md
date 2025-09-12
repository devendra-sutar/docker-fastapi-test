# Docker FastAPI Test

A simple FastAPI application running in Docker & Docker Compose.  
Stores user data in a JSON file (`data/users.json`). No database required.

# Features
- `GET /` — returns a hello message  
- `GET /users` — returns list of users stored in JSON file  
- `POST /users` — accepts user data (`id`, `name`, `username`, `email`) and stores it  
- `DELETE /users/{id}` — deletes a user by their ID  
- Data persists across container stops/restarts thanks to mapped `data/` folder  

# Project Structure
1.  Clone the repository  
    git clone https://github.com/<your-username>/docker-fastapi-test.git
    cd docker-fastapi-test
2.  Build & run the Docker containers
    cd docker-fastapi-test
    docker-compose up --build -d
3.  Check containers status
    docker ps
4.  Create a user
   curl -X POST "http://localhost:8000/users" \
    -H "Content-Type: application/json" \
    -d '{"id": 1, "name": "John Doe", "username": "john_doe", "email": "john.doe@example.com"}'

