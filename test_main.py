from main import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["service"] == "tasks-api"


def test_list_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_add_task():
    client = app.test_client()
    response = client.post(
        "/tasks",
        json={"title": "test task"}
    )
    assert response.status_code == 201
    assert response.get_json()["task"]["title"] == "test task"


def test_reject_empty_task():
    client = app.test_client()
    response = client.post("/tasks", json={})
    assert response.status_code == 400
