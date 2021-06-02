import datetime

from pydantic import BaseModel


class BaseStatus(BaseModel):
    title: str


class Status(BaseStatus):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class StatusCreate(BaseStatus):
    """Status Create"""


class StatusUpdate(BaseStatus):
    """Status Update"""
