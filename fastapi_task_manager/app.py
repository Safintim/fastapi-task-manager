from fastapi import FastAPI
from fastapi_task_manager.api.router import router

app = FastAPI()
app.include_router(router)


@app.get('/')
def root():
    return {'message': 'Hello'}
