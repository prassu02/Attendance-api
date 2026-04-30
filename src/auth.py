from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = "secret"
ALGO = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict, hours: int = 24):
    data["exp"] = datetime.utcnow() + timedelta(hours=hours)
    return jwt.encode(data, SECRET_KEY, algorithm=ALGO)