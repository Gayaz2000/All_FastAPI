from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from typing_extensions import List

app = FastAPI()

books = [
  {
    "id": 1,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
    "language": "English",
    "published_date": "1960-07-11"
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell",
    "genre": "Dystopian",
    "language": "English",
    "published_date": "1949-06-08"
  },
  {
    "id": 3,
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "genre": "Adventure",
    "language": "Portuguese",
    "published_date": "1988-04-15"
  },
  {
    "id": 4,
    "title": "One Hundred Years of Solitude",
    "author": "Gabriel García Márquez",
    "genre": "Magical Realism",
    "language": "Spanish",
    "published_date": "1967-06-05"
  },
  {
    "id": 5,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic",
    "language": "English",
    "published_date": "1925-04-10"
  },
  {
    "id": 6,
    "title": "Kafka on the Shore",
    "author": "Haruki Murakami",
    "genre": "Fantasy",
    "language": "Japanese",
    "published_date": "2002-09-12"
  },
  {
    "id": 7,
    "title": "The Kite Runner",
    "author": "Khaled Hosseini",
    "genre": "Drama",
    "language": "English",
    "published_date": "2003-05-29"
  },
  {
    "id": 8,
    "title": "Crime and Punishment",
    "author": "Fyodor Dostoevsky",
    "genre": "Philosophical Fiction",
    "language": "Russian",
    "published_date": "1866-01-01"
  },
  {
    "id": 9,
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "genre": "Romance",
    "language": "English",
    "published_date": "1813-01-28"
  },
  {
    "id": 10,
    "title": "The Little Prince",
    "author": "Antoine de Saint-Exupéry",
    "genre": "Children's Literature",
    "language": "French",
    "published_date": "1943-04-06"
  }
]

class Books(BaseModel):
    id : int
    title: str
    author: str
    genre: str
    language: str
    published_date: str

class BooksUpdateData(BaseModel):
    id : int
    title: str
    author: str
    genre: str
    language: str
    published_date: str

#Reading
@app.get("/books", response_model= List[Books])
async def get_all_books()->dict:
    return books

#Creating
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Books)->dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get("/books/{book_id}")
async def get_book(book_id: int)->dict:
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#updating       
@app.patch("/books/{book_id}")
async def get_book(book_id: int, book_update_data: BooksUpdateData)->dict:
    pass

#Deleting
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
          books.remove(book)
          return {}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")