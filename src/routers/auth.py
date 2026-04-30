from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.models import User
from src.auth import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth")

@router.post("/signup")
def signup(email: str, password: str, role: str):
    db: Session = SessionLocal()
    user = User(email=email, password=hash_password(password), role=role)
    db.add(user)
    db.commit()
    return {"msg": "created"}

@router.post("/login")
def login(email: str, password: str):
    db: Session = SessionLocal()
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(401)

    return {"token": create_token({"user_id": user.id, "role": user.role})}