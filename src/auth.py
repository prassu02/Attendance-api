from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def create_token(data: dict, expires_delta: int = 24):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(hours=expires_delta)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)