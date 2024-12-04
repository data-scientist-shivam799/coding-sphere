import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    """
    Tests that a user can be registered with the expected response.
    """
    response = client.post("/auth/register", json={
        "username": "testuser",
        "password": "password123",
        "role": "user"
    })
    assert response.status_code == 200
    assert response.json().get("message") == "User registered successfully"