from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

books = [
    {"id": 1, "title": "Асинхронность в Python", "author": "Стен Ли"},
    {"id": 2, "title": "Backend на Python", "author": "Бен Робин"},
]

@app.get("/books")
def read_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

class NewBook(BaseModel):
    id: str
    title: str
    author: str

@app.post("/books")
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {"success": True, "message": "Книга успешно добавлена"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(i)
            return {"success": True, "message": "Книга удалена"}
    raise HTTPException(status_code=404, detail="Книга не найдена")