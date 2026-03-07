from pydantic import BaseModel,EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

class User(BaseModel):
    name: str
    email: EmailStr


class UserCreate(User):
    password:str


class Login(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    created_at: datetime

    # Pydantic V2 syntax
    model_config = ConfigDict(from_attributes=True)




class NoteCreate(BaseModel):
    title: str
    content: str


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoteDelete(BaseModel):
    title: str


class NoteResponse(BaseModel):
    title: str
    content: str
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

 




