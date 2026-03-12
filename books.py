
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="The ID is not needed on create", default=None)
    title: str = Field(min_length=10)
    author: str = Field(min_length=5)
    description: str = Field(min_length=10)
    rating: int = Field(ge=0, le=6)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "new book title",
                "author": "new book author",
                "description": "new book description",
                "rating": 5
            }
        }
    }

BOOKS = [
    Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "A novel about the American dream.", 5),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "A novel about racial injustice in the Deep South.", 5),
    Book(3, "1984", "George Orwell", "A dystopian novel about totalitarianism.", 4),
    Book(4, "Moby Dick", "Herman Melville", "A novel about the quest for revenge against a giant white whale.", 4),
    Book(5, "Pride and Prejudice", "Jane Austen", "A novel about love and social class in 19th century England.", 5),
    Book(6, "The Catcher in the Rye", "J.D. Salinger", "A novel about teenage rebellion and alienation.", 4),
    Book(7, "The Lord of the Rings", "J.R.R. Tolkien", "A fantasy novel about the quest to destroy a powerful ring.", 5),
]


# GET all books
@app.get("/books")
async def get_all_books():
    try:
        return BOOKS
    except Exception as e:
        return {"error": str(e)}
    
# GET book by id
@app.get("/books/getbookbyid/{id}")
async def get_book_by_id(id: int):
    try:
        for book in BOOKS:
            if book.id == id:
                return book
        return {"error": "Book not found"}
    except Exception as e:
        return {"error": str(e)}
    
# POST create book
@app.post("/books/createbook")
async def add_book(book_request: BookRequest):
    try:
        new_book = Book(**book_request.model_dump())
        find_book_id(new_book)
        BOOKS.append(new_book)
        return BOOKS
    except Exception as e:
        return {"error": str(e)}
    
# Function which finds the id of the book and adds it to the book object before adding it to the list of books
def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1