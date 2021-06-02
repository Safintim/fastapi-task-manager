from fastapi import APIRouter

from fastapi_task_manager.api.auth import router as auth_router
from fastapi_task_manager.api.labels import router as labels_router
from fastapi_task_manager.api.statuses import router as statuses_router

router = APIRouter()
router.include_router(labels_router)
router.include_router(statuses_router)
router.include_router(auth_router)
