import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from fastapi_task_manager.database import engine

Base = declarative_base()

USERNAME_MAX_LENGTH = 150
TITLE_MAX_LENGTH = 100


class CommonFields:
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(TITLE_MAX_LENGTH))
    created_at = sa.Column(sa.DateTime(), default=datetime.datetime.now)


class Label(CommonFields, Base):
    __tablename__ = 'labels'


class Status(CommonFields, Base):
    __tablename__ = 'statuses'


class Task(CommonFields, Base):
    __tablename__ = 'tasks'

    description = sa.Column(sa.Text)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    status_id = sa.Column(sa.Integer, sa.ForeignKey('statuses.id'))
    label_id = sa.Column(sa.Integer, sa.ForeignKey('labels.id'))


class User(CommonFields, Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime(), default=datetime.datetime.now)
    first_name = sa.Column(sa.String(USERNAME_MAX_LENGTH))
    last_name = sa.Column(sa.String(USERNAME_MAX_LENGTH))
    username = sa.Column(sa.String(USERNAME_MAX_LENGTH), unique=True)
    password_hash = sa.Column(sa.Text)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
