from fastapi import APIRouter, HTTPException, Request
from src.auth import create_token

router = APIRouter()

API_KEY = "MY_SECRET_KEY"

@router.post("/auth/monitoring-token")
def monitoring_token(request: Request, key: str):
    user = request.state.user
    if user["role"] != "monitoring_officer":
        raise HTTPException(403)

    if key != API_KEY:
        raise HTTPException(401)

    return {"token": create_token({"role": "monitoring"}, 1)}

@router.get("/monitoring/attendance")
def get_monitoring(request: Request):
    user = require(["monitoring"])(request)
    return {"data": "readonly"}

@router.post("/monitoring/attendance")
def block():
    raise HTTPException(405)