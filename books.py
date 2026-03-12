
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_year: int
    
    def __init__(self, id, title, author, description, rating, published_year):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_year = published_year
        

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="The ID is not needed on create", default=None)
    title: str = Field(min_length=10)
    author: str = Field(min_length=5)
    description: str = Field(min_length=10)
    rating: int = Field(ge=0, le=6)
    published_year: int = Field(ge=1200, le=2027)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "new book title",
                "author": "new book author",
                "description": "new book description",
                "rating": 5,
                "published_year": 2020
            }
        }
    }

BOOKS = [
    Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "A novel about the American dream.", 5, 2020),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "A novel about racial injustice in the Deep South.", 5, 1999),
    Book(3, "1984", "George Orwell", "A dystopian novel about totalitarianism.", 4, 1915),
    Book(4, "Moby Dick", "Herman Melville", "A novel about the quest for revenge against a giant white whale.", 4, 1700),
    Book(5, "Pride and Prejudice", "Jane Austen", "A novel about love and social class in 19th century England.", 5, 2021),
    Book(6, "The Catcher in the Rye", "J.D. Salinger", "A novel about teenage rebellion and alienation.", 4, 2022),
    Book(7, "The Lord of the Rings", "J.R.R. Tolkien", "A fantasy novel about the quest to destroy a powerful ring.", 5, 2016),
]


# GET all books
@app.get("/books", status_code=status.HTTP_200_OK)
async def get_all_books():
    try:
        return BOOKS
    except Exception as e:
        return {"error": str(e)}
    
# GET book by id
@app.get("/books/id/{id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(id: int = Path(gt=0)):
    try:
        for book in BOOKS:
            if book.id == id:
                return book
        raise HTTPException(status_code=404, detail="Book not found")
    except Exception as e:
        return {"error": str(e)}
    
# GET book by rating
@app.get("/books/rating/", status_code=status.HTTP_200_OK)
async def get_book_by_rating(rating: int = Query(ge=0, le=6)):
    books_founded = []
    try:
        for book in BOOKS:
            if book.rating == rating:
                books_founded.append(book)
        return books_founded
    except Exception as e:
        return {"message": str(e)}

#GET book by published year
@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def get_book_by_year(published_year: int = Query(ge=1200, le=2027)):
    books_founded = []
    try:
        for book in BOOKS:
            if book.published_year == published_year:
                books_founded.append(book)
        if books_founded:
            return books_founded
        else:
            return {"message": f"No books of year {published_year} found."}
    except Exception as e:
        return {"message": str(e)}
    
# POST create book
@app.post("/books/createbook", status_code=status.HTTP_201_CREATED)
async def add_book(book_request: BookRequest):
    try:
        new_book = Book(**book_request.model_dump())
        find_book_id(new_book)
        BOOKS.append(new_book)
        return BOOKS
    except Exception as e:
        return {"error": str(e)}
    
# UPDATE book with PUT request
@app.put("/books/updatebook", status_code=status.HTTP_200_OK)
async def update_book(book: BookRequest):
    book_changed = False
    try:
        for i in range(len(BOOKS)):
            if BOOKS[i].id == book.id:
                BOOKS[i] = book
                book_changed = True
        if not book_changed:
            raise HTTPException(status_code=404, detail="Book not found")     
        return BOOKS
    except Exception as e:
        return {"message": str(e)}
    
# DELETE book with DELETE request
@app.delete("/books/deletebook/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    try:
        for i in range(len(BOOKS)):
            if book_id == BOOKS[i].id:
                BOOKS.pop(i)
                book_changed = True
                break
        if not book_changed:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"message": f"Book with id {book_id} deleted.", "books": BOOKS}
    except Exception as e:
        return {"message": str(e)}
    
# Function which finds the id of the book and adds it to the book object before adding it to the list of books
def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1