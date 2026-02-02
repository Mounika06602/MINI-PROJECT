from fastapi import APIRouter
from database import notes_coll
from bson import ObjectId
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
    return notes_coll.find_one({"title":title})
    
@router.get("/read")
def read(title: str):
    return notes_coll.find_one({"title": title})


 
