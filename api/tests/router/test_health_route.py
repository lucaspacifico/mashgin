from fastapi.testclient import TestClient

from app.main import app
from app.settings import Settings

client = TestClient(app)
settings = Settings()


def test_health():
    response = client.get("/")
    assert response.status_code == 200


def test_additional_health_route():
    response = client.get("/health")
    assert response.status_code == 200
