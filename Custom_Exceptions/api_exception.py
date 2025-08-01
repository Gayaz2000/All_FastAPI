from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/divide")
async def divide(a:  float, b: float):
    if b == 0:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="Division by zero is not allowed")
    return {"result": a/b}

class NotFoundException(Exception):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

from fastapi.responses import JSONResponse
from fastapi.requests import Request

@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code= status.HTTP_400_BAD_REQUEST,
        content={"message": f"Oops! {exc.name} not found"}
    )

items = {"apple": 10, "banana": 20, "orange": 30}

@app.get("/items/{item_name}")
async def get_item(item_name: str):
    if item_name not in items:
        raise NotFoundException(item_name)
    return {"item": item_name, "price": items[item_name]}