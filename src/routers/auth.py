from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.utils.auth import hash_password, verify_password, create_token

router = APIRouter()

# ===== Request Models =====
class SignupRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str


# ===== Fake DB (for assignment demo) =====
fake_users_db = {}


# ===== SIGNUP =====
@router.post("/signup")
def signup(data: SignupRequest):
    if data.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pwd = hash_password(data.password)

    fake_users_db[data.username] = {
        "username": data.username,
        "password": hashed_pwd
    }

    return {"message": "User created successfully"}


# ===== LOGIN =====
@router.post("/login")
def login(data: LoginRequest):
    user = fake_users_db.get(data.username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_token({"sub": data.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
