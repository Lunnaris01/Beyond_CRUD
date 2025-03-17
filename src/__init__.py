from fastapi import FastAPI
from src.books.routes import book_router
from src.db.main import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def life_span(app:FastAPI):
    print("Starting Server...")
    await init_db()
    yield
    print("Server has been stopped")


version = "v0.0.1"

app = FastAPI(
    title = "Bookly",
    description="A REST API for books",
	version=version,
	lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books")