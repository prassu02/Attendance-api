@router.post("/auth/monitoring-token")
def monitoring_token(api_key: str, user=Depends(role_required(["monitoring_officer"]))):
    if api_key != "MY_SECRET_KEY":
        raise HTTPException(status_code=401)
    
    return {"token": create_token({"role": "monitoring"}, 1)}