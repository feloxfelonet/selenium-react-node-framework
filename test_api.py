import requests
import pytest

BASE_URL = "http://localhost:5000"

@pytest.fixture(scope="module")
def session():
    return requests.Session()

def test_login_valid(session):
    res = session.post(f"{BASE_URL}/login", json={"username": "admin", "password": "admin"})
    assert res.status_code == 200
    assert res.json()["success"] == True

def test_login_invalid(session):
    res = session.post(f"{BASE_URL}/login", json={"username": "admin", "password": "wrong"})
    assert res.status_code == 401
    assert res.json()["success"] == False

def test_post_item(session):
    payload = {"name": "Test Task"}
    res = session.post(f"{BASE_URL}/items", json=payload)
    assert res.status_code == 201
    json_data = res.json()
    assert json_data["name"] == "Test Task"
    global item_id
    item_id = json_data["id"]

def test_get_items(session):
    res = session.get(f"{BASE_URL}/items")
    assert res.status_code == 200
    assert any(item["name"] == "Test Task" for item in res.json())

def test_update_item(session):
    updated = {"name": "Updated Task"}
    res = session.put(f"{BASE_URL}/items/{item_id}", json=updated)
    assert res.status_code == 200
    assert res.json()["name"] == "Updated Task"

def test_delete_item(session):
    res = session.delete(f"{BASE_URL}/items/{item_id}")
    assert res.status_code == 204

def test_get_invalid_endpoint(session):
    res = session.get(f"{BASE_URL}/nonexistent")
    assert res.status_code == 404