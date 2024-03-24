from fastapi import FastAPI, HTTPException
from typing import List, Optional
from models import User, Gender, Role
from uuid import UUID, uuid4
app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "user"}

db: List[User] = [
    User(id=uuid4(), 
        first_name = "Jon",
        last_name = "Jones",
        gender = Gender.male
        ),
    User(id=uuid4(), 
        first_name = "Alex",
        last_name = "Volk",
        middle_name = "The Great",
        gender = Gender.male,
        role = [Role.admin, Role.student]
        ),
    User(id=uuid4(), 
        first_name = "Valentina",
        middle_name = "Bullet",
        gender = Gender.female,
        role = [Role.user]
        ),
    User(id=uuid4(), 
        first_name = "Izzy",
        gender = Gender.male
        )
]

@app.get("/users")
async def show_users():
    return db

@app.delete("/users/{userProf}")
async def delete_user(userProf: UUID):
    for user in db:
        if user.id==userProf:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"User {userProf} not found"
    )
@app.post("/users")
async def insert_user(user: User):
    db.append(user)
    return {"Added": user.first_name}

@app.put("/users/{userID}")
async def update_user(userID: UUID, userProf: User):
    for user in db:
        if user.id==userID:
            if user.first_name is not None:
                user.first_name = userProf.first_name
            if user.middle_name is not None:
                user.middle_name = userProf.middle_name
            if user.second_name is not None:
                user.second_name = userProf.second_name
            if user.gender is not None:
                user.gender = userProf.gender
            if user.role is not None:
                user.role = userProf.role
            return
    raise HTTPException(
        status_code=404,
        detail=f"User {userProf} not found"
    )
