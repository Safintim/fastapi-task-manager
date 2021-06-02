import uvicorn

from fastapi_task_manager.settings import settings

uvicorn.run(
    'fastapi_task_manager.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
