import pytest
from httpx import AsyncClient

from app.main import app


@pytest.fixture
def mock_token(mocker):
    return mocker.patch("jwt.decode")


@pytest.mark.asyncio
async def test_admin_route_with_valid_token(mock_token):
    # GIVEN
    mock_token.return_value = {"role": "admin", "sub": "admin"}

    # WHEN
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/admin", headers={"Authorization": "Bearer abc123"})

    # THEN
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome, Admin!"}


@pytest.mark.asyncio
async def test_admin_route_with_invalid_token():
    # GIVEN

    # WHEN
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/admin")

    # THEN
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}
