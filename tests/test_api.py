from fastapi.testclient import TestClient
from src.main import app

c=TestClient(app)

def test_signup():
    r=c.post("/auth/signup",json={"name":"a","email":"a@a.com","password":"123","role":"student"})
    assert r.status_code==200

def test_login():
    r=c.post("/auth/login",json={"email":"a@a.com","password":"123"})
    assert "token" in r.json()

def test_no_token():
    assert c.post("/batches",json={"name":"x","institution_id":1}).status_code in [401,403]

def test_monitor_405():
    assert c.post("/monitoring/attendance").status_code in [404,405]

def test_attendance_forbidden():
    assert c.post("/attendance/mark",json={"session_id":1,"status":"present"}).status_code in [401,403]