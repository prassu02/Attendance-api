from fastapi import APIRouter
from src.utils.auth import hash_password, verify_password, create_token

router = APIRouter()

@router.post("/signup")
def signup():
    return {"message": "Signup working"}

@router.post("/login")
def login():
    return {"message": "Login working"}
