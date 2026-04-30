from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import User
from ..schemas import Signup,Login
from ..auth import hash_password,verify_password,create_token

router=APIRouter()

def db():
    d=SessionLocal();yield d;d.close()

@router.post("/auth/signup")
def signup(data:Signup,db:Session=Depends(db)):
    if db.query(User).filter(User.email==data.email).first():
        raise HTTPException(400)
    u=User(**data.dict(),password=hash_password(data.password))
    db.add(u);db.commit()
    return {"token":create_token({"user_id":u.id,"role":u.role})}

@router.post("/auth/login")
def login(data:Login,db:Session=Depends(db)):
    u=db.query(User).filter(User.email==data.email).first()
    if not u or not verify_password(data.password,u.password):
        raise HTTPException(401)
    return {"token":create_token({"user_id":u.id,"role":u.role})}