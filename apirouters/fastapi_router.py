from fastapi import APIRouter
from pydantic import BaseModel, Field

book_router = APIRouter()

class BookCreateModel(BaseModel):
    title: str = Field(description="The title of the created book")
    author: str = Field(description="The creator of the book")

@book_router.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }