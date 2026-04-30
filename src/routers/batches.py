@app.post("/batches")
def create_batch(request: Request):
    user = verify(request)
    if user["role"] not in ["trainer", "institution"]:
        raise HTTPException(status_code=403)
    return {"msg": "batch created"}