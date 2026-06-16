from fastapi import FastAPI
from app.routers import users
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(users.router)