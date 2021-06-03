import datetime

from pydantic import BaseModel


class BaseTask(BaseModel):
    title: str
    description: str
    status_id: int
    label_id: int
    user_id: int


class Task(BaseTask):
    """Task Get/List"""
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class TaskCreate(BaseTask):
    """Task Create"""


class TaskUpdate(BaseTask):
    """Task Update"""
