from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_signup():
    r = client.post("/auth/signup?email=a&password=1&role=student")
    assert r.status_code == 200

def test_login():
    client.post("/auth/signup?email=a&password=1&role=student")
    r = client.post("/auth/login?email=a&password=1")
    assert r.status_code == 200

def test_protected():
    token = client.post("/auth/login?email=a&password=1").json()["token"]
    r = client.post("/attendance/mark", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code in [200, 403]

def test_no_token():
    r = client.post("/attendance/mark")
    assert r.status_code == 401

def test_monitoring_block():
    r = client.post("/monitoring/attendance")
    assert r.status_code == 405