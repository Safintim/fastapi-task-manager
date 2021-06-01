from fastapi import APIRouter
from fastapi_task_manager.models.labels import Label

router = APIRouter(
    prefix='/labels',
)


@router.get('/', response_model=list[Label])
def get_labels():
    return []
