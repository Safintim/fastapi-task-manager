from fastapi_task_manager.models.statuses import StatusCreate
from fastapi import Depends, HTTPException
from fastapi import status as fastapi_status
from sqlalchemy.orm import Session

from fastapi_task_manager import tables
from fastapi_task_manager.database import get_session


class StatusesService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def get(self, status_id) -> tables.Status:
        return self._get(status_id)

    def get_list(self) -> list[tables.Status]:
        return self.session.query(tables.Status).all()

    def create(self, status_data: StatusCreate) -> tables.Status:
        status = tables.Status(**status_data.dict())
        self.session.add(status)
        self.session.commit()
        return status

    def update(self, status_id, status_data) -> tables.Status:
        status = self._get(status_id)
        for field, value in status_data:
            setattr(status, field, value)
        self.session.commit()
        return status

    def delete(self, status_id) -> None:
        status = self._get(status_id)
        self.session.delete(status)
        self.session.commit()

    def _get(self, status_id: int) -> tables.Status:
        status = self.session.query(
            tables.Status,
        ).filter_by(id=status_id).first()
        if not status:
            raise HTTPException(status_code=fastapi_status.HTTP_404_NOT_FOUND)
        return status
