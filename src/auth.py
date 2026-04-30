from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from .config import SECRET_KEY, ALGORITHM

pwd = CryptContext(schemes=["bcrypt"])

def hash_password(p): return pwd.hash(p)
def verify_password(p,h): return pwd.verify(p,h)

def create_token(data, mins=1440):
    d=data.copy()
    d["exp"]=datetime.utcnow()+timedelta(minutes=mins)
    return jwt.encode(d,SECRET_KEY,algorithm=ALGORITHM)

def decode_token(t):
    return jwt.decode(t,SECRET_KEY,algorithms=[ALGORITHM])