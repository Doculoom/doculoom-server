from fastapi import FastAPI

from app.routers import docs, health

app = FastAPI()

app.include_router(docs.router, prefix="/docs", tags=["docs"])
app.include_router(health.router, prefix="/health", tags=["health"])

