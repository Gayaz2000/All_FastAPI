from pydantic import BaseModel, Field

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