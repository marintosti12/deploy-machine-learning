from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root_ok():
    r = client.get("/")
    assert r.status_code == 200