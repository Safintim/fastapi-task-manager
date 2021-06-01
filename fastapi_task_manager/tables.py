import datetime

import sqlalchemy as sa
from fastapi_task_manager.database import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Label(Base):
    __tablename__ = 'labels'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(100))
    created_at = sa.Column(sa.DateTime(), default=datetime.datetime.utcnow)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
