import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils import create_jwt

client = TestClient(app)

# Helper function to create JWT tokens for testing
def get_token(role):
    """Generate a JWT token with a specific role."""
    payload = {
        "user_id": "test_user_id",
        "role": role
    }
    return create_jwt(payload)

def test_get_projects_as_user():
    """Test: User role can access the GET /projects endpoint."""
    token = get_token("user")
    response = client.get(
        "/projects",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_projects_as_admin():
    """Test: Admin role can access the GET /projects endpoint."""
    token = get_token("admin")
    response = client.get(
        "/projects",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_project_as_admin():
    """Test: Admin role can create a project."""
    token = get_token("admin")
    response = client.post(
        "/projects",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Project A", "description": "Description of Project A"}
    )
    assert response.status_code == 200
    assert response.json().get("message") == "Project created"

def test_create_project_as_user():
    """Test: User role cannot create a project."""
    token = get_token("user")
    response = client.post(
        "/projects",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Project A", "description": "Description of Project A"}
    )
    assert response.status_code == 403
    assert response.json().get("detail") == "Access forbidden"