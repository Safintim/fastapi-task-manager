from fastapi import APIRouter, Depends, Response, status

from fastapi_task_manager.models.tasks import Task, TaskCreate, TaskUpdate
from fastapi_task_manager.models.auth import User
from fastapi_task_manager.services.auth import get_current_user
from fastapi_task_manager.services.tasks import TasksService

router = APIRouter(prefix='/tasks')


@router.get('/{task_id}', response_model=Task)
def get_task(
    task_id: int,
    user: User = Depends(get_current_user),
    service: TasksService = Depends(),
):
    return service.get(task_id)


@router.get('/', response_model=list[Task])
def get_tasks(
    user: User = Depends(get_current_user),
    service: TasksService = Depends(),
):
    return service.get_list()


@router.post('/', response_model=Task)
def create_task(
    task_data: TaskCreate,
    user: User = Depends(get_current_user),
    service: TasksService = Depends(),
):
    return service.create(task_data)


@router.put('/{task_id}', response_model=Task)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    user: User = Depends(get_current_user),
    service: TasksService = Depends(),
):
    return service.update(task_id, task_data)


@router.delete('/{task_id}')
def delete_task(
    task_id: int,
    user: User = Depends(get_current_user),
    service: TasksService = Depends(),
):
    service.delete(task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
