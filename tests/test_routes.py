from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_unit():
    response = client.get("/cards/unit/188")
    assert response.status_code == 200
    assert response.json()["Name"] == "4-LOM"

def test_get_leader():
    response = client.get("/cards/leader/009")
    assert response.status_code == 200
    assert response.json()["Name"] == "Leia Organa"