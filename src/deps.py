from fastapi import Request, HTTPException
from jose import jwt

SECRET_KEY = "secret"

def get_user(request: Request):
    auth = request.headers.get("Authorization")
    if not auth:
        raise HTTPException(401)

    token = auth.split(" ")[1]
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

def require(role_list):
    def wrapper(request: Request):
        user = get_user(request)
        if user["role"] not in role_list:
            raise HTTPException(403)
        return user
    return wrapper