# FastAPI Books API

This project is a simple REST API to manage a collection of books, built with FastAPI.

## Features

- List all books
- Search book by ID
- Add a new book (ID assigned automatically)
- Data validation with Pydantic

## Requirements

- Python 3.8 or higher
- FastAPI
- Uvicorn

## Installation

```bash
pip install fastapi uvicorn
```

## Running

```bash
uvicorn Books:app --reload
```

## Main Endpoints

- List all books: `GET /books`
- Search book by ID: `GET /books/getbookbyid/{id}`
- Add book: `POST /books/createbook`

## Example book object

```json
{
  "title": "Example Book Title",
  "author": "Author Name",
  "description": "Brief description of the book.",
  "rating": 5
}
```

---

Developed to practice CRUD operations with FastAPI.
