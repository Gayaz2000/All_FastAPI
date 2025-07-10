from sqlalchemy import Column, Integer, String, Float
from Basic.fastapi_crud import Base  

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True, nullable=False, index=True)
    price = Column(Float, nullable=False)
    quality = Column(Integer, default=0)
