from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Attendance,BatchStudent,Session as S
from ..schemas import AttendanceCreate
from ..deps import role_required

router=APIRouter()

def db(): d=SessionLocal();yield d;d.close()

@router.post("/attendance/mark")
def mark(data:AttendanceCreate,db:Session=Depends(db),
user=Depends(role_required(["student"]))):
    s=db.query(S).filter_by(id=data.session_id).first()
    if not s: raise HTTPException(404)

    if not db.query(BatchStudent).filter_by(
        batch_id=s.batch_id,student_id=user["user_id"]).first():
        raise HTTPException(403)

    a=Attendance(session_id=s.id,student_id=user["user_id"],
                 status=data.status)
    db.add(a);db.commit()
    return {"msg":"marked"}