from fastapi import FastAPI

app = FastAPI(title="Users Service")

users = []

@app.get("/users")
def list_users():
    return users

@app.post("/users")
def create_user(user: dict):
    user["id"] = len(users) + 1
    users.append(user)
    return user

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return next((u for u in users if u["id"] == user_id), None)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    for i, u in enumerate(users):
        if u["id"] == user_id:
            user["id"] = user_id
            users[i] = user
            return user
    return {"error": "Not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "Deleted"}