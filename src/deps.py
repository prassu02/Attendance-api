from fastapi import Depends, HTTPException
from jose import jwt

def get_current_user(token: str):
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401)

def role_required(roles: list):
    def wrapper(user=Depends(get_current_user)):
        if user["role"] not in roles:
            raise HTTPException(status_code=403)
        return user
    return wrapper