from database import notes_coll, users_coll
from bson import ObjectId
from fastapi import APIRouter
router = APIRouter()
"""
Notes

create - post 
update - put
read - get
delete - delete


"""


@router.post("/create")
def create(title:str, content:str):
    result = notes_coll.insert_one({"title":title,"content":content})
    return {"message": "Note created", "id": str(result.inserted_id)}


@router.get("/get")
def get(title: str):
    note=notes_coll.find_one({"title":title})
    return note
    
@router.get("/read")
def read(title: str):
    return notes_coll.find_one({"title": title})

# Update route
@router.put("/update")
def update(title: str, new_title: str, new_content: str):
    notes_coll.update_one(
        {"title": title},
        {"$set": {"title": new_title, "content": new_content}}
    )
    return {"message": "Note updated"}

# Delete route  
@router.delete("/delete")
def delete(title: str):
    notes_coll.delete_one({"title": title})
    return {"message": "Note deleted"}


@router.post("/users/create")
def create_user(username: str, email: str, password: str):
    result = users_coll.insert_one({"username": username, "email": email, "password": password})
    return {"message": "User created"}

@router.get("/users/get")
def get_user(username: str):
    return users_coll.find_one({"username": username})

@router.put("/users/update")
def update_user(username: str, new_username: str, new_email: str):
    users_coll.update_one(
        {"username": username},
        {"$set": {"username": new_username, "email": new_email}}
    )
    return {"message": "User updated"}

@router.delete("/users/delete")
def delete_user(username: str):
    users_coll.delete_one({"username": username})
    return {"message": "User deleted"}