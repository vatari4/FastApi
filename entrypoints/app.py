from fastapi import FastAPI
from contextlib import asynccontextmanager
from infrastructure.database.session import create_tables, delete_tables
from infrastructure.api.controllers import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database cleared")
    await create_tables()
    print("Database ready")
    yield
    print("Shutting down")

def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(tasks_router)
    return app