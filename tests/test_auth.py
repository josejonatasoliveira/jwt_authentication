import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.models import User
from app.security.dependencies import get_password_hash

client = TestClient(app)


@pytest.fixture
def mock_jwt_encode(mocker):
    return mocker.patch("jwt.encode", return_value="ok")


@pytest.fixture
def mock_jwt_decode(mocker):
    return mocker.patch("jwt.decode", return_value={"sub": "admin", "role": "admin"})


def test_auth_with_valid_credentials(mocker, mock_jwt_encode):
    # GIVEN
    form_data = {
        "username": "admin",
        "password": "JKSipm0YH"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    mocker.patch("app.security.auth.authenticate_user",
                 return_value = User(username="admin", hashed_password=get_password_hash("JKSipm0YH"), role="admin"))

    # WHEN
    response = client.post("/token", data=form_data, headers=headers)

    # THEN
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_auth_with_invalid_credentials(mocker, mock_jwt_encode):
    # GIVEN
    form_data = {
        "username": "admin",
        "password": "JKSipm0YH"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    mocker.patch("app.security.auth.authenticate_user",
                 return_value = None)

    # WHEN
    response = client.post("/token", data=form_data, headers=headers)

    # THEN
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"


def test_protected_route_with_auth(mocker, mock_jwt_encode, mock_jwt_decode):
    # GIVEN
    form_data = {
        "username": "admin",
        "password": "JKSipm0YH"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    user = User(username="admin", hashed_password=get_password_hash("JKSipm0YH"), role="admin")
    mocker.patch("app.security.auth.authenticate_user",
                 return_value = user)

    mocker.patch("app.security.dependencies.get_current_user",
                 return_value = user)

    # WHEN
    response = client.post("/token", data=form_data, headers=headers)
    token = response.json()["access_token"]

    response = client.get("/admin", headers={"Authorization": f"Bearer {token}"})

    # THEN
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome, Admin!"
