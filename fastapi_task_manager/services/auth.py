from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from fastapi_task_manager import tables
from fastapi_task_manager.database import get_session
from fastapi_task_manager.models.auth import Token, User, UserCreate
from fastapi_task_manager.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/sign-in/')


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return AuthService.validate_token(token)


class AuthService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def register_new_user(self, user_data: UserCreate) -> Token:
        user = tables.User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            username=user_data.username,
            password_hash=self.hash_password(user_data.password),
        )

        self.session.add(user)
        self.session.commit()
        return self.create_token(user)

    def authenticate(self, username: str, password: str) -> Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={
                'WWW-Authenticate': 'Bearer',
            },
        )
        user = self.session.query(tables.User).filter(
            tables.User.username == username,
        ).first()

        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={
                'WWW-Authenticate': 'Bearer',
            },
        )
        try:
            payload = jwt.decode(
                token=token,
                key=settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except jwt.JWTError as ex:
            raise exception from ex

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError as exc:
            raise exception from exc

        return user

    @classmethod
    def create_token(cls, user: tables.User) -> Token:
        user_data = User.from_orm(user)
        now = datetime.utcnow()
        user_data = user_data.dict()
        user_data['created_at'] = user_data['created_at'].isoformat()
        payload = {
            'iat': now,  # время выпуска
            'nbf': now,  # начало действия
            'exp': now + timedelta(seconds=settings.jwt_expiration),
            'sub': str(user_data['id']),
            'user': user_data,
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return Token(access_token=token)
