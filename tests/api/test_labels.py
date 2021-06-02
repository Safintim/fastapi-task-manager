from fastapi.testclient import TestClient

from fastapi_task_manager.app import app

client = TestClient(app)


def test_get_labels():
    response = client.get('/labels')
    assert response.status_code == 200
