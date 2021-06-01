from datetime import datetime

from pydantic import BaseModel


class Label(BaseModel):
    id: int
    title: str
    created_at: datetime
