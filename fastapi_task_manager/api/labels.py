from fastapi import APIRouter, Depends, Response, status

from fastapi_task_manager.models.labels import Label, LabelCreate, LabelUpdate
from fastapi_task_manager.services.labels import LabelsService

router = APIRouter(prefix='/labels')


@router.get('/{label_id}', response_model=Label)
def get_label(
    label_id: int,
    service: LabelsService = Depends(),
):
    return service.get(label_id)


@router.get('/', response_model=list[Label])
def get_labels(service: LabelsService = Depends()):
    return service.get_list()


@router.post('/', response_model=Label)
def create_label(
    label_data: LabelCreate,
    service: LabelsService = Depends(),
):
    return service.create(label_data)


@router.put('/{label_id}', response_model=Label)
def update_label(
    label_id: int,
    label_data: LabelUpdate,
    service: LabelsService = Depends(),
):
    return service.update(label_id, label_data)


@router.delete('/{label_id}')
def delete_label(
    label_id: int,
    service: LabelsService = Depends(),
):
    service.delete(label_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
