# Request Body

## 1) When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
## 2) 2) A request body is data sent by the client to your API. A response body is the data your API sends to the client.
## 3) To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.
##Note:
### Sending a body with a GET request has an undefined behavior in the specifications, nevertheless, it is supported by FastAPI, only for very complex/extreme use cases.

from fastapi import FastAPI
import nest_asyncio
nest_asyncio.apply()

app = FastAPI()

from pydantic import BaseModel, Field

class BookCreateModel(BaseModel):
    title: str = Field(description="The title of the created book")
    author: str = Field(description="The creator of the book")

@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }

