import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from fastapi_task_manager.database import engine

Base = declarative_base()


class CommonFields:
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(100))
    created_at = sa.Column(sa.DateTime(), default=datetime.datetime.now)


class Label(CommonFields, Base):
    __tablename__ = 'labels'


class Status(CommonFields, Base):
    __tablename__ = 'statuses'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
