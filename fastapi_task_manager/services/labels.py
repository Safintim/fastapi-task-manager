from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from fastapi_task_manager import tables
from fastapi_task_manager.database import get_session
from fastapi_task_manager.models.labels import LabelCreate, LabelUpdate


class LabelsService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def get(self, label_id) -> tables.Label:
        return self._get(label_id)

    def get_list(self) -> list[tables.Label]:
        return self.session.query(tables.Label).all()

    def create(self, label_data: LabelCreate) -> tables.Label:
        label = tables.Label(**label_data.dict())
        self.session.add(label)
        self.session.commit()
        return label

    def update(self, label_id: int, label_data: LabelUpdate) -> tables.Label:
        label = self._get(label_id)
        for field, value in label_data:
            setattr(label, field, value)
        self.session.commit()
        return label

    def delete(self, label_id: int) -> None:
        label = self._get(label_id)
        self.session.delete(label)
        self.session.commit()

    def _get(self, label_id: int) -> tables.Label:
        label = self.session.query(tables.Label).filter_by(id=label_id).first()
        if not label:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return label
