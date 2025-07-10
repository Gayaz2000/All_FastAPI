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

class CreateUser(BaseModel):
    user_name = str
    password = str

class UserLogin(BaseModel):
    user_name : str
    password : str