from pydantic import BaseModel, EmailStr

class Signup(BaseModel):
    name:str; email:EmailStr; password:str; role:str

class Login(BaseModel):
    email:EmailStr; password:str

class BatchCreate(BaseModel):
    name:str; institution_id:int

class InviteJoin(BaseModel):
    token:str

class SessionCreate(BaseModel):
    batch_id:int; trainer_id:int; title:str; date:str

class AttendanceCreate(BaseModel):
    session_id:int; status:str