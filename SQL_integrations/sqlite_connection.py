# ORM --> Object Relational Mapper

from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional, List
from fastapi import FastAPI
from contextlib import asynccontextmanager

# Define model
class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = False

# Setup DB
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# FastAPI app with lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# POST endpoint to add item
@app.post("/items/")
async def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

# GET endpoint to list items
@app.get("/items/", response_model=List[Item])
async def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
