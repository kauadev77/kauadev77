from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health() -> None:
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_echo_normalizes_message() -> None:
    response = client.post("/v1/echo", json={"message": "  hello   world  "})
    assert response.status_code == 200
    assert response.json()["message"] == "hello world"
