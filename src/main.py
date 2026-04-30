from fastapi import FastAPI
from .database import Base,engine
from .routes import auth,batches,sessions,attendance,summaries,monitoring

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(auth.router)
app.include_router(batches.router)
app.include_router(sessions.router)
app.include_router(attendance.router)
app.include_router(summaries.router)
app.include_router(monitoring.router)