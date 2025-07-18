from fastapi import FastAPI, HTTPException

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Ассинхроность в Python",
        "author": "Стен Ли"
    },
    {
        "id": 2,
        "title": "Backend на Python",
        "author": "Бен Робин"
    },
]

@app.get(
        "/books",
        tags=["Книги"],
        summary="Получить все книги"
        )
def read_books():
    return books


@app.get(
        "/books/{book_id}",
        tags=["Книги"],
        summary="Получить конретную книжку"
        )
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Книга не найдена")


@app.post("/books")
def create_book():
    