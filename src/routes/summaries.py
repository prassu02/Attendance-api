from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import SessionLocal
from ..models import Attendance,Session as S,Batch
from ..deps import role_required

router=APIRouter()

def db(): d=SessionLocal();yield d;d.close()

@router.get("/batches/{id}/summary")
def batch_summary(id:int,db:Session=Depends(db),
user=Depends(role_required(["institution"]))):
    total=db.query(func.count(Attendance.id)).join(S).filter(S.batch_id==id).scalar()
    return {"batch_id":id,"attendance":total}

@router.get("/programme/summary")
def prog(db:Session=Depends(db),
user=Depends(role_required(["programme_manager"]))):
    total=db.query(func.count(Attendance.id)).scalar()
    return {"total_attendance":total}