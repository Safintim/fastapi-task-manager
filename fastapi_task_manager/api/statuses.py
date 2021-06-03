from fastapi import APIRouter, Depends, Response
from fastapi import status as fastapi_status

from fastapi_task_manager.models.auth import User
from fastapi_task_manager.models.statuses import (
    Status,
    StatusCreate,
    StatusUpdate,
)
from fastapi_task_manager.services.auth import get_current_user
from fastapi_task_manager.services.statuses import StatusesService

router = APIRouter(prefix='/statuses')


@router.get('/{status_id}', response_model=Status)
def get_status(
    status_id: int,
    user: User = Depends(get_current_user),
    service: StatusesService = Depends(),
):
    return service.get(status_id)


@router.get('/', response_model=list[Status])
def get_statuses(
    user: User = Depends(get_current_user),
    service: StatusesService = Depends(),
):
    return service.get_list()


@router.post('/', response_model=Status)
def create_status(
    status_data: StatusCreate,
    user: User = Depends(get_current_user),
    service: StatusesService = Depends(),
):
    return service.create(status_data)


@router.put('/{status_id}', response_model=Status)
def update_status(
    status_id: int,
    status_data: StatusUpdate,
    user: User = Depends(get_current_user),
    service: StatusesService = Depends(),
):
    return service.update(status_id, status_data)


@router.delete('/{status_id}')
def delete_status(
    status_id: int,
    user: User = Depends(get_current_user),
    service: StatusesService = Depends(),
):
    service.delete(status_id)
    return Response(status_code=fastapi_status.HTTP_204_NO_CONTENT)
