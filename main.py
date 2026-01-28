
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models import NoteSchema
from bson import ObjectId

app = FastAPI()

# Database Connection
client = MongoClient("mongodb://localhost:27017")
db = client.notes_db

@app.post("/notes/")
async def create_note(note: NoteSchema):
    new_note = note.dict()
    result = db.notes.insert_one(new_note)
    return {"id": str(result.inserted_id), **new_note}

@app.get("/notes/")
async def get_active_notes():
    # Only fetch notes where is_deleted is False
    notes = list(db.notes.find({"is_deleted": False}))
    for note in notes:
        note["_id"] = str(note["_id"]) # Convert ObjectId to string for JSON
    return notes







                        
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)