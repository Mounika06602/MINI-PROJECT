from fastapi import APIRouter, HTTPException, status
from database import users_coll
from schemas import UserCreate, Login
from models import hash_password, verify_password
from datetime import datetime

router = APIRouter()


# CREATE USER
@router.post("/signup", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):

    data = user.model_dump()   # convert pydantic → dictionary

    # check if user already exists
    if users_coll.find_one({"email": data["email"]}):
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    # hash password
    data["password"] = hash_password(data["password"])

    # add created time
    data["created_at"] = datetime.utcnow()

    users_coll.insert_one(data)

    return {"message": "User created successfully"}


# LOGIN USER
@router.post("/login")
def login(credentials: Login):

    data = credentials.model_dump()

    user = users_coll.find_one({"email": data["email"]})

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(data["password"], user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    return {"message": "Login successful"}


# UPDATE USERNAME
@router.put("/update")
def update_user(email: str, new_username: str):

    result = users_coll.update_one(
        {"email": email},
        {"$set": {"name": new_username}}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"message": "Username updated successfully"}


# DELETE USER
@router.delete("/delete")
def delete_user(email: str):

    result = users_coll.delete_one({"email": email})

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"message": "User deleted successfully"}
