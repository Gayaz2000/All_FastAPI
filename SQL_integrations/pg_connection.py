##  PostGres Connection

postgres_uri = ""   # Enter Conection uri
from sqlmodel import SQLModel, Field
from contextlib import asynccontextmanager

class Item(SQLModel, table = True):
    id : int = Field(description="id for records", primary_key= True)
    name: str
    price: float
    is_offer: bool = False

from sqlmodel import create_engine, Session
from fastapi import FastAPI

engine = create_engine(postgres_uri, echo= True)

def create_db_and_tables():
    "Creates DB and Table"
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables
    yield

app = FastAPI(lifespan= lifespan)

@app.post("/items/")
async def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh()
        return item
    
from typing_extensions import List
from sqlmodel import select

@app.get("/items/", response_model= Item)
async def get_item():
    with Session(engine) as session:
        items = session.exec(select(List[Item])).all()
        return items 