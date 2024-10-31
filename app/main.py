from fastapi import FastAPI
from app.database import database, engine
from app.models import Base
import app.endpoints.clients as clients

app = FastAPI()

app.include_router(clients.router)


@app.on_event("startup")
async def startup():
    await database.connect()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
