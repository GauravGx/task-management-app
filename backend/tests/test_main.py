from fastapi.testclient import TestClient
from app.main import app

#fastapi application ko test karne ke liye test client banaya
client = TestClient(app)



def test_home():
    #Actual server manually start kiye bina / endpoint ko request bheji.
    response = client.get("/")
    #Expected status 200 hai.
    assert response.status_code ==200
    #Response ka actual JSON bhi verify kar rahe hain.
    assert response.json() =={
        "message": "Task Management API is running"
    }

def test_get_tasks():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Get Test Task",
            "description": "Testing get task",
            "user_id": 1
        }
    )

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id

def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Testing API",
            "user_id": 1
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Test Task"
    assert data["description"] == "Testing API"
    assert data["is_completed"] is False
    assert data["user_id"] == 1   



def test_get_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Get Test Task",
            "description": "Testing get task",
            "user_id": 1
        }
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_update_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Update Test Task",
            "description": "Testing update task",
            "user_id": 1
        }
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated Test Task",
            "description": "Updated description",
            "is_completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Updated Test Task"
    assert data["description"] == "Updated description"
    assert data["is_completed"] is True   



def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Delete Test Task",
            "description": "Testing delete task",
            "user_id": 1
        }
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 404



def test_create_task_invalid_title():
    response = client.post(
        "/tasks",
        json={
            "title": "a",
            "description": "Valid description",
            "user_id": 1
        }
    )

    assert response.status_code == 422   

def test_create_task_missing_title():
    response = client.post(
        "/tasks",
        json={
            "description": "Valid description",
            "user_id": 1
        }
    )

    assert response.status_code == 422     

def test_get_nonexistent_task():
    response = client.get("/tasks/999999")

    assert response.status_code == 404    