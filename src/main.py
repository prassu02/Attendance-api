print("App starting...")

from fastapi import FastAPI
from src.database import Base, engine
from src.routes import auth, batches, sessions, attendance, summaries, monitoring

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(batches.router)
app.include_router(sessions.router)
app.include_router(attendance.router)
app.include_router(summaries.router)
app.include_router(monitoring.router)