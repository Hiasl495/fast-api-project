from fastapi import FastAPI
from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User, UpdateUser
from uuid import UUID
from fastapi import HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
# This is a sample Python script.

@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(status_code=404, detail=f"Delete user failed, id {id} not found.")

@app.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
                if user_update.last_name is not None:
                    user.last_name = user_update.last_name
                    if user_update.roles is not None:
                        user.roles = user_update.roles
                        return user.id
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Insert User objects into in-memory DB
db: List[User] = [User(
    id=uuid4(),
    first_name="John",
    last_name="Doe",
    gender=Gender.male,
    roles=[Role.user],
 ),

 User(
    id=uuid4(),
    first_name="Jane",
    last_name="Doe",
    gender=Gender.female,
    roles=[Role.user],
 ),

 User(
    id=uuid4(),
    first_name="James",
    last_name="Gabriel",
    gender=Gender.male,
    roles=[Role.user],
 ),
 User(
    id=uuid4(),
    first_name="Eunit",
    last_name="Eunit",
    gender=Gender.male,
    roles=[Role.admin, Role.user],
 ),
]
