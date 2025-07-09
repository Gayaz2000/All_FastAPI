## MySQL Integration

MYSQL_URI = ""

from sqlmodel import SQLModel, Field

class Item(SQLModel, table= True):
    id: int = Field(primary_key= True)
    name: str
    salary: float
    is_offer: bool = False

from sqlmodel import create_engine

engine = create_engine(MYSQL_URI, echo= True)

from fastapi import FastAPI
from contextlib import asynccontextmanager

def create_db_and_tabels():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tabels
    yield

app = FastAPI(lifespan= lifespan)

from sqlmodel import Session, select
from typing_extensions import List

@app.post("/items/")
async def create_table(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh()
        return item
    
@app.get("/items/", response_model= Item)
async def read_table():
    with Session(engine) as session:
        items = session.exec(select(List[Item])).all()
        return items