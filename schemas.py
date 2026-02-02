from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "user"

 
class Login(BaseModel):
    email: EmailStr
    password: str



class Notes(BaseModel):
    id: object
    title: str
    content: str
    Createdat: datetime
    Updatedat: datetime