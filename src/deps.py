from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from .auth import decode_token

security=HTTPBearer()

def get_user(token=Depends(security)):
    try: return decode_token(token.credentials)
    except: raise HTTPException(401)

def role_required(roles):
    def check(user=Depends(get_user)):
        if user["role"] not in roles:
            raise HTTPException(403)
        return user
    return check