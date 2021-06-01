from fastapi import APIRouter
from fastapi_task_manager.api.labels import router as labels_router

router = APIRouter()
router.include_router(labels_router)
