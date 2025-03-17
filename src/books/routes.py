
from fastapi import FastAPI, Header, status, APIRouter
from fastapi.exceptions import HTTPException
from typing import Optional, List
from pydantic import BaseModel
from src.books.bookdata import books
from src.books.schemas import Book,BookUpdate

book_router = APIRouter()


@book_router.get('/', response_model = List[Book])
async def get_all_books():
	return books

@book_router.get('/{book_id}')
async def get_book(book_id:int) -> dict:
	for book in books:
		if book["id"] == book_id:
			return book
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.post('/', status_code = status.HTTP_201_CREATED)
async def add_book(book_data:Book)->dict:
	bookentry = book_data.model_dump()
	books.append(bookentry)
	return bookentry

@book_router.patch('/{book_id}')
async def update_book(book_id:int, book_data:Book) -> dict:
	for i, book in enumerate(books):
		if book["id"] == book_id:
			books[i] = book_data.model_dump()
			return {}
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.delete("/{book_id}")
async def delete_book(book_id:int):
	for i, book in enumerate(books):
		if book["id"] == book_id:
			books.remove(i)
			return {}
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
