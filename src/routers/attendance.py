@router.post("/attendance/mark")
def mark(request: Request):
    user = require(["student"])(request)
    return {"msg": "marked"}