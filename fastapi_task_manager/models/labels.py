import datetime

from pydantic import BaseModel


class LabelBase(BaseModel):
    title: str


class Label(LabelBase):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class LabelCreate(LabelBase):
    """Label Create"""


class LabelUpdate(LabelBase):
    """Label Update"""
