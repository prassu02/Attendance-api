from fastapi import APIRouter, Depends
from src.deps import role_required

router = APIRouter()

@router.post("/sessions")
def create_session(user=Depends(role_required(["trainer"]))):
    return {"message": "Session Created"}