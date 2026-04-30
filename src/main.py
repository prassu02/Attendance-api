from fastapi import FastAPI

app = FastAPI()

from src.routes.auth import router as auth_router
from src.routes.sessions import router as session_router
from src.routes.attendance import router as attendance_router
from src.routes.monitoring import router as monitoring_router

@app.get("/")
def home():
    return {"message": "API is running"}

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(session_router, prefix="/sessions", tags=["Sessions"])
app.include_router(attendance_router, prefix="/attendance", tags=["Attendance"])
app.include_router(monitoring_router, prefix="/monitoring", tags=["Monitoring"])
