from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"messages": "Hello World"}

#Path Parameter
# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     return {"item_id": item_id}

#Query Parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None): # Any additional parameter in function is called a 'Query'
    return {"item_id": item_id, "query": q}

@app.get("/products/")
async def list_products(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}