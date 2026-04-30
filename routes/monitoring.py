from fastapi import APIRouter,HTTPException,Header
from ..auth import create_token,decode_token
from ..config import MONITORING_API_KEY

router=APIRouter()

@router.post("/auth/monitoring-token")
def gen(key:str):
    if key!=MONITORING_API_KEY:
        raise HTTPException(401)
    return {"token":create_token({"role":"monitoring"},60)}

@router.get("/monitoring/attendance")
def read(x_token:str=Header(...)):
    p=decode_token(x_token)
    if p["role"]!="monitoring":
        raise HTTPException(401)
    return {"data":"read-only"}