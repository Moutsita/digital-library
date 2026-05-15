from fastapi import FastAPI

app = FastAPI(title="Books Service")

books = []

@app.get("/books")
def list_books():
    return books

@app.post("/books")
def create_book(book: dict):
    book["id"] = len(books) + 1
    books.append(book)
    return book

@app.get("/books/{book_id}")
def get_book(book_id: int):
    return next((b for b in books if b["id"] == book_id), None)

@app.put("/books/{book_id}")
def update_book(book_id: int, book: dict):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            book["id"] = book_id
            books[i] = book
            return book
    return {"error": "Not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    global books
    books = [b for b in books if b["id"] != book_id]
    return {"message": "Deleted"}

@app.get("/books/search")
def search_books(q: str):
    return [b for b in books if q.lower() in b.get("title", "").lower()]