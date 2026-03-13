from pydantic import BaseModel, EmailStr
from datetime import datetime


# -------------------------
# USER CREATE
# -------------------------
class UserCreate(BaseModel):

    name: str
    email: EmailStr
    password: str


# -------------------------
# USER LOGIN
# -------------------------
class UserLogin(BaseModel):

    email: EmailStr
    password: str


# -------------------------
# USER RESPONSE
# -------------------------
class UserResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True