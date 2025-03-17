from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from pydantic import BaseModel
from bookdata import books

app = FastAPI()

class Book(BaseModel):
		id: int
		title: str
		author: str
		publisher: str
		published_date: str
		page_count: int
		language: str



@app.get('/books', response_model = List[Book])
async def get_all_books():
	return books

@app.get('/books/{book_id}')
async def get_book(book_id:int) -> dict:
	for book in books:
		if book["id"] == book_id:
			return book
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.post('/books', status_code = status.HTTP_201_CREATED)
async def add_book(book_data:Book)->dict:
	bookentry = book_data.model_dump()
	books.append(bookentry)
	return bookentry

@app.patch('/books/{book_id}')
async def update_book(book_id:int, book_data:Book) -> dict:
	for i, book in enumerate(books):
		if book["id"] == book_id:
			books[i] = book_data.model_dump()
			return {}
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/books/{book_id}")
async def delete_book(book_id:int):
	for i, book in enumerate(books):
		if book["id"] == book_id:
			books.remove(i)
			return {}
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
