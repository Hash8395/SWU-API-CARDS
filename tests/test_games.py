from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_game():
    response = client.post("/games/create", params={"deck": "test", "visibility": "public"})
    assert response.status_code == 401  # Simule une session non connectée