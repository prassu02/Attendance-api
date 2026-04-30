from fastapi import APIRouter, HTTPException, Request
from src.auth import create_token
from src.deps import get_user

router = APIRouter()

API_KEY = "MY_SECRET_KEY"

# 🔐 Generate monitoring token
@router.post("/auth/monitoring-token")
def monitoring_token(request: Request, key: str):
    user = get_user(request)

    if user["role"] != "monitoring_officer":
        raise HTTPException(status_code=403, detail="Not allowed")

    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {"token": create_token({"role": "monitoring"}, 1)}


# 👁️ Read-only monitoring endpoint
@router.get("/monitoring/attendance")
def get_monitoring(request: Request):
    user = get_user(request)

    if user["role"] != "monitoring":
        raise HTTPException(status_code=401, detail="Invalid monitoring token")

    return {"data": "monitoring attendance (read-only)"}


# 🚫 Block other methods
@router.post("/monitoring/attendance")
def block_post():
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@router.put("/monitoring/attendance")
def block_put():
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@router.delete("/monitoring/attendance")
def block_delete():
    raise HTTPException(status_code=405, detail="Method Not Allowed")
