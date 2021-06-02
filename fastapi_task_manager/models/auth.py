import datetime

from pydantic import BaseModel


class Baseuser(BaseModel):
    username: str
    first_name: str
    last_name: str


class UserCreate(Baseuser):
    password: str


class User(Baseuser):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
