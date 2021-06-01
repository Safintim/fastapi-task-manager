import uvicorn

uvicorn.run(
    'fastapi_task_manager.app:app',
    reload=True,
)
