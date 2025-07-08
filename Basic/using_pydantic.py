from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False
    password: str = "Don't show password"

class ItemResponse(BaseModel):
    name: str
    price: float
    is_offer: bool = False

#Creat Funtion
@app.post("/items/", response_model=ItemResponse)
async def create_items(item: Item):
    return item