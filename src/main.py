from fastapi import FastAPI

# CREATE APP (ONLY ONCE)
app = FastAPI(
    title="Attendance API",
    version="1.0.0"
)

# IMPORT ROUTERS
from src.routes.auth import router as auth_router
from src.routes.sessions import router as session_router
from src.routes.attendance import router as attendance_router
from src.routes.monitoring import router as monitoring_router

# ROOT ENDPOINT
@app.get("/")
def home():
    return {"message": "API is running"}

# HEALTH CHECK (important for production)
@app.get("/health")
def health():
    return {"status": "ok"}

# INCLUDE ROUTERS
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(session_router, prefix="/sessions", tags=["Sessions"])
app.include_router(attendance_router, prefix="/attendance", tags=["Attendance"])
app.include_router(monitoring_router, prefix="/monitoring", tags=["Monitoring"])
