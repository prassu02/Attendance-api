from fastapi import FastAPI
from src.database import Base, engine

app = FastAPI()

# 🔥 Safe table creation
try:
    Base.metadata.create_all(bind=engine)
    print("DB connected")
except Exception as e:
    print("DB INIT ERROR:", e)

# 🔥 Safe router imports
try:
    from src.routers import auth, sessions, attendance, monitoring

    app.include_router(auth.router)
    app.include_router(sessions.router)
    app.include_router(attendance.router)
    app.include_router(monitoring.router)

    print("Routers loaded")
except Exception as e:
    print("ROUTER ERROR:", e)

@app.get("/")
def home():
    return {"msg": "API running"}
