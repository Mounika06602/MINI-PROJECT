"""from pymongo import MongoClient
from datetime import datetime
import sys

import os

uri = os.getenv("MONGODB_URI")

db = os.getenv("DB_NAME")
user = os.getenv("USERS")
notes = os.getenv("NOTES")

connection = MongoClient(uri)
database= connection["db"]
collections= database["user"]
collections.insert_one({
    "name": "Mouni",
    "email": "mouni@123.com",
    "password": "1234566555",
    "status": "active"
})
print(collections)
"""

from pymongo import MongoClient
import os
from dotenv import load_dotenv
from database import notes_coll, users_coll
load_dotenv()



"""
mongo conection
db
collections - users, notes
MONGODB_URI= mongodb+srv://Mounika:mouni123@cluster0.82umbdb.mongodb.net/?appName=Cluster0
DB_NAME= Notes_DB
USERS = NOTES_USERS
NOTES= SMART_NOTES

"""

uri = os.getenv("MONGODB_URI")

db = os.getenv("DB_NAME")
user = os.getenv("USERS")
notes = os.getenv("NOTES")

connection = MongoClient(uri)

database = connection[db]
notes_coll = database[notes]









from pymongo import MongoClient
from datetime import datetime
import os
uri = os.getenv("MongoDB_URL")
db = os.getenv("DB_NAME")
user = os.getenv("Users")
notes = os.getenv("NOTES")

connection = MongoClient(uri)
database= connection["db"]
collections= database["user"]
collections.insert_one({
    "name": "Mouni",
    "email": "mouni@123.com",
    "password": "1234566555",
    "status": "active"
})




if not user: return {"Log in": "Failed"} # No user found if user["password"] == password: return {"Log in": "Successful"} else: return {"Log in": "Not Matched"}

@router.put("/update")
def update_user(email: str, new_username: Optional[str], new_email: Optional[str], new_password:str):
    users_coll.update_one(
        {"email": email},
        {"$set": {"username": new_username, "email": new_email}}
    )
    return {"message": "User updated"}


    class UpdateUser(BaseModel):
     email: str
    new_username: Optional[str] = None
    new_email: Optional[str] = None
    new_password: Optional[str] = None

@router.put("/update")
def update_user(user: UpdateUser):
    update_fields = {}
    if user.new_username:
        update_fields["username"] = user.new_username
    if user.new_email:
        update_fields["email"] = user.new_email
    if user.new_password:
        update_fields["password"] = user.new_password

    if update_fields:
        users_coll.update_one(
            {"email": user.email},
            {"$set": update_fields}
        )
        return {"message": "User updated"}
    else:
        return {"message": "No fields to update"}
    





    user_routes.py
    from fastapi import APIRouter
from database import users_coll
from typing import Optional

router = APIRouter()

@router.post("/signup")
def create_user(username: str, email: str, password: str):
    user  = users_coll.find_one({"email":email})
    print(user)
    if user.email == email:
        return {"user":"already ecists"}
    
    result = users_coll.insert_one({"username": username, "email": email, "password": password})
    return {"message": "User created"}

@router.get("/login")
def get_user( email: str, password: str):
    user = users_coll.find_one({"email":email})
    if not user:
        return {"Log in": "Failed"}
    if user["password"] == password: 
        return {"Log in": "Successful"} 
    else: 
        return {"Log in": "Not Matched"}
    
@router.put("/update")
def update_user(email: str, new_username: Optional[str], new_email: Optional[str], new_password:str):
    users_coll.update_one(
        {"email": email},
        {"$set": {"username": new_username, "email": new_email}}
    )
    return {"message": "User updated"}

    




@router.delete("/delete")
def delete_user(username: str):
    users_coll.delete_one({"username": username})
    return {"message": "User deleted"}




/-------notes routes.py-------#

from database import notes_coll
from fastapi import APIRouter
from bson import ObjectId
router = APIRouter()



@router.post("/create")
def create(title:str, content:str):
    result = notes_coll.insert_one({"title":title,"content":content})
    return {"message": "Note created", "id": str(result.inserted_id)}

@router.get("/get") 
def get(title: str): 
    note = notes_coll.find_one({"title": title})
    if note: 
      
        note["_id"] = str(note["_id"])# Convert ObjectId to string 
        return note 
    else: 
        return {"message": "Note not found"}



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







from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from database import notes_coll
from typing import Optional
from schemas import User, Login ,Notes
from schemas import MessageResponse
from datetime import datetime,timezone
from bson import ObjectId
from fastapi import status


router = APIRouter()


@router.post("/create", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)

def create(title: str, content: str):

    try:
        result = notes_coll.insert_one({
            "title": title,
            "content": content
        })

        return {
            "message": "Note created successfully",
            "id": str(result.inserted_id)
        }

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create note"
        )

@router.get("/get")
def get(title: str):

    try:
        note = notes_coll.find_one({"title": title})

        if not note:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Note not found"
            )

        note["_id"] = str(note["_id"])
        return note

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving note"
        )
    
from schemas import NoteResponse
@router.get("/all", response_model=list[NoteResponse])
def get_all_notes():
    try:
        
        notes = list(notes_coll.find())
        for note in notes:
            note["_id"] = str(note["_id"])
        return notes
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to fetch notes")

@router.put("/update", response_model=MessageResponse)
def update(title: str, new_title: str, new_content: str):

    try:
        result = notes_coll.update_one(
            {"title": title},
            {"$set": {"title": new_title, "content": new_content}}
        )

        if result.matched_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Note not found"
            )

        return {"message": "Note updated successfully"}

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update note"
        )


@router.delete("/delete", response_model=MessageResponse)
def delete(title: str):

    try:
        result = notes_coll.delete_one({"title": title})

        if result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Note not found"
            )

        return {"message": "Note deleted successfully"}

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete note"
        )







from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from database import users_coll
from typing import Optional
from schemas import User, Login
from schemas import MessageResponse
from datetime import datetime,timezone
from bson import ObjectId

router = APIRouter()



@router.post("/signup")
def create_user(user: User):
    existing_user = users_coll.find_one({"email" :  user.email})
    if existing_user:
        raise HTTPException(status_code=400,detail="User already exists")
    new_user = {
        "Username": user.Username,
        "email": user.email,
        "password": user.password,
        "Createdat": datetime.now(timezone.utc)
    }
    result = users_coll.insert_one(new_user)
    return {"message": "User Created Succesfully",
            "id": str(result.inserted_id)}
     

@router.get("/login")
def login_user(login: Login):
    user = users_coll.find_one({"email": Login.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user["password"] == Login.password:
        raise HTTPException(status_code=401, detail="Password not matched")
    
    return {"message": "Login successful"}

       
@router.put("/update", response_model=MessageResponse)
def update_user(
    email: str,
    new_username: Optional[str] = None,
    new_email: Optional[str] = None,
    new_password: Optional[str] = None
):

    user = users_coll.find_one({"email": email})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = {}

    if new_username:
        update_data["Username"] = new_username
    if new_email:
        update_data["email"] = new_email
    if new_password:
        update_data["password"] = new_password

    users_coll.update_one(
        {"email": email},
        {"$set": update_data}
    )

    return {"message": "User updated successfully"}

@router.delete("/delete", response_model=MessageResponse)
def delete_user(username: str):

    result = users_coll.delete_one({"Username": username})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}
