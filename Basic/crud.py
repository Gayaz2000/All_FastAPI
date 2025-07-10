from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from Basic.fastapi_crud import engine, SessionLocal
from utils.models import Base, Item
from sqlalchemy.orm import Session

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Schema
class ItemSchema(BaseModel):
    name: str
    price: float
    quality: int

class ItemResponse(ItemSchema):
    id: int

    class Config:
        orm_mode = True  # Allow returning SQLAlchemy model as Pydantic

# Create
@app.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, quality=item.quality, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Read
@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Update
@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemSchema, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.quality = item.quality
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item

# Delete
@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": f"Item '{db_item.name}' successfully deleted"}
