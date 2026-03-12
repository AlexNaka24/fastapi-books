# FastAPI Books API

This project is a simple REST API to manage a collection of books, built with FastAPI.

# Books API

REST API to manage a collection of books using FastAPI.

## Features

- List all books
- Get book by ID
- Get books by rating
- Get books by published year
- Create a new book
- Update an existing book
- Delete a book by ID

## Installation

1. Clone the repository:
  ```bash
  git clone <REPO_URL>
  cd mi-nuevo-proyecto
  ```

2. Create and activate a virtual environment:
  ```bash
  python -m venv .venv
  # On Windows:
  .venv\Scripts\activate
  # On Linux/Mac:
  source .venv/bin/activate
  ```

3. Install dependencies:
  ```bash
  pip install fastapi uvicorn pydantic
  ```

## Usage

1. Start the server:
  ```bash
  uvicorn books:app --reload
  ```

2. Open the interactive documentation at:
  - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Main Endpoints

| Method | Endpoint                        | Description                      |
|--------|----------------------------------|----------------------------------|
| GET    | `/books`                        | List all books                   |
| GET    | `/books/id/{id}`                | Get book by ID                   |
| GET    | `/books/rating/{rating}`        | Get books by rating              |
| GET    | `/books/publish/{published_year}` | Get books by published year      |
| POST   | `/books/createbook`             | Create a new book                |
| PUT    | `/books/updatebook`             | Update an existing book          |
| DELETE | `/books/deletebook/{book_id}`   | Delete a book by ID              |

## Example Book Object

```json
{
  "title": "The Example Book",
  "author": "John Doe",
  "description": "A sample book for demonstration purposes.",
  "rating": 4,
  "published_year": 2023
}
```

## Example Requests

### Create a Book

**POST** `/books/createbook`

Request body:
```json
{
  "title": "The Example Book",
  "author": "John Doe",
  "description": "A sample book for demonstration purposes.",
  "rating": 4,
  "published_year": 2023
}
```

### Get Books by Rating

**GET** `/books/rating/4`

Response:
```json
[
  {
   "id": 3,
   "title": "1984",
   "author": "George Orwell",
   "description": "A dystopian novel about totalitarianism.",
   "rating": 4,
   "published_year": 1915
  },
  {
   "id": 4,
   "title": "Moby Dick",
   "author": "Herman Melville",
   "description": "A novel about the quest for revenge against a giant white whale.",
   "rating": 4,
   "published_year": 1700
  },
  {
   "id": 6,
   "title": "The Catcher in the Rye",
   "author": "J.D. Salinger",
   "description": "A novel about teenage rebellion and alienation.",
   "rating": 4,
   "published_year": 2022
  }
]
```

### Delete a Book

**DELETE** `/books/deletebook/3`

Response:
```json
{
  "message": "Book with id 3 deleted.",
  "books": [
   // ...remaining books
  ]
}
```
