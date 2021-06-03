from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from fastapi_task_manager import tables
from fastapi_task_manager.database import get_session
from fastapi_task_manager.models.tasks import TaskCreate, TaskUpdate


class TasksService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def get(self, task_id: int) -> tables.Task:
        return self._get(task_id)

    def get_list(self) -> list[tables.Task]:
        return self.session.query(tables.Task).all()

    def create(self, task_data: TaskCreate) -> tables.Task:
        task = tables.Task(**task_data.dict())
        self.session.add(task)
        self.session.commit()
        return task

    def update(self, task_id: int, task_data: TaskUpdate) -> tables.Task:
        task = self._get(task_id)
        for field, value in task_data:
            setattr(task, field, value)
        self.session.commit()
        return task

    def delete(self, task_id: int) -> None:
        task = self._get(task_id)
        self.session.delete(task)
        self.session.commit()

    def _get(self, task_id: int) -> tables.Task:
        task = self.session.query(tables.Task).filter_by(id=task_id).first()
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return task
