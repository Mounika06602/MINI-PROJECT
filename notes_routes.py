from database import notes_coll
from fastapi import APIRouter, HTTPException, status
from schemas import NoteCreate,NoteResponse,NoteUpdate,NoteDelete

router = APIRouter()

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create(data: NoteCreate):

    data = data.model_dump()

    if notes_coll.find_one({"title": data["title"]}):
        raise HTTPException(status_code=400, detail="Note with this title already exists")

    result = notes_coll.insert_one(data)

    return {"message": "Note created", "id": str(result.inserted_id)}


@router.get("/note")
def get(data: NoteDelete):

    data = data.model_dump()

    note = notes_coll.find_one({"title": data["title"]})

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note["_id"] = str(note["_id"])

    return note


@router.put("/update")
def update(data: NoteUpdate):

    data = data.model_dump()

    result = notes_coll.update_one(
        {"title": data["title"]},
        {"$set": {"title": data["new_title"], "content": data["new_content"]}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Note not found to update")

    return {"message": "Note updated"}


@router.delete("/delete")
def delete(data: NoteDelete):

    data = data.model_dump()

    result = notes_coll.delete_one({"title": data["title"]})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Note deleted"}
    