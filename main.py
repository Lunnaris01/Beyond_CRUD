from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()



@app.get('/')
async def read_root():
	return {"message": "Hello World"}

@app.get("/greet")
async def greet_user(name:Optional[str] = "User") -> dict:
	return {"message": f"Hello {name}"}

@app.get("/greet/{name}")
async def greet_user_with_query(name:str) -> dict:
	return {"message": f"Hello {name}"}

class BookCreateModel(BaseModel):
	title : str	
	author : str


@app.post("/books")
async def create_book(book_data:BookCreateModel):
	return {
		"title": book_data.title,
		"author": book_data.author
	}

@app.get('/get_headers', status_code = 200)
async def get_headers(
	accept:str = Header(None),
	content_type: str = Header(None),
	content_length: str = Header(None)
):
	request_headers = {}
	request_headers["Accept"] = accept
	request_headers["Content-Type"] = content_type
	request_headers["Content-Length"] = content_length
	return request_headers