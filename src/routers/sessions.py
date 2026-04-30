@router.post("/sessions")
def create_session(request: Request):
    user = require(["trainer"])(request)
    return {"msg": "session created"}