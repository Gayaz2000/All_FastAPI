# ORM --> Object Relational Mapper

from sqlmodel import SQLModel, Field
from typing_extensions import Optional
from contextlib import asynccontextmanager

class Items(SQLModel, table = True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str
    price: float
    is_offer: bool = False

from sqlmodel import create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo= True)

async def create_and_():
    """Creates Database"""