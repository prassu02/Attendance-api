from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Session as S
from ..schemas import SessionCreate
from ..deps import role_required

router=APIRouter()

def db(): d=SessionLocal();yield d;d.close()

@router.post("/sessions")
def create(data:SessionCreate,db:Session=Depends(db),
user=Depends(role_required(["trainer"]))):
    s=S(**data.dict());db.add(s);db.commit()
    return {"msg":"created","id":s.id}