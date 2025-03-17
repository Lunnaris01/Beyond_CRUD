from fastapi import FastAPI
from src.books.routes import book_router

version = "v0.0.1"

app = FastAPI(
    title = "Bookly",
    description="A REST API for books",
	version=version
)
app.include_router(book_router, prefix=f"/api/{version}/books")