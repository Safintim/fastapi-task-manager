from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm

from fastapi_task_manager.models.auth import Token, User, UserCreate
from fastapi_task_manager.services.auth import AuthService, get_current_user

router = APIRouter(prefix='/auth')


@router.post('/sign-up', response_model=Token)
def sign_up(
    user_data: UserCreate,
    service: AuthService = Depends(),
):
    return service.register_new_user(user_data)


@router.post('/sign-in', response_model=Token)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(),
):
    return service.authenticate(
        form_data.username,
        form_data.password,
    )


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user
