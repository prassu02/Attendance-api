from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
import secrets
from ..database import SessionLocal
from ..models import Batch,BatchInvite,BatchStudent
from ..schemas import BatchCreate,InviteJoin
from ..deps import role_required

router=APIRouter()

def db(): d=SessionLocal();yield d;d.close()

@router.post("/batches")
def create(data:BatchCreate,db:Session=Depends(db),
user=Depends(role_required(["trainer","institution"]))):
    b=Batch(**data.dict());db.add(b);db.commit()
    return {"msg":"created","id":b.id}

@router.post("/batches/{id}/invite")
def invite(id:int,db:Session=Depends(db),
user=Depends(role_required(["trainer"]))):
    token=secrets.token_hex(8)
    inv=BatchInvite(batch_id=id,token=token,
    created_by=user["user_id"],
    expires_at=datetime.utcnow()+timedelta(days=1))
    db.add(inv);db.commit()
    return {"token":token}

@router.post("/batches/join")
def join(data:InviteJoin,db:Session=Depends(db),
user=Depends(role_required(["student"]))):
    inv=db.query(BatchInvite).filter_by(token=data.token,used=False).first()
    if not inv or inv.expires_at<datetime.utcnow():
        raise HTTPException(400)
    db.add(BatchStudent(batch_id=inv.batch_id,student_id=user["user_id"]))
    inv.used=True;db.commit()
    return {"msg":"joined"}