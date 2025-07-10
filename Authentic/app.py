from fastapi import FastAPI, HTTPException, status
from passlib.context import CryptContext
from db import database, metadata, engine
from api_auth import users
from schemas.state_schemas import CreateUser, UserLogin

app = FastAPI()
metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/register")
async def register(user: CreateUser):
    query = users.select().where(users.c.username == user.user_name)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="User already exist")
    hashed_password = pwd_context.hash(user.password)
    query = users.insert().values(username = user.user_name, password = hashed_password)
    await database.execute(query)
    return {"message":"User Created Successfully."}

@app.post("/login")
async def login(user: UserLogin):
    query = users.select().where(users.c.username == user.user_name)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="User already exist")
    
    if not pwd_context.verify(user.password, existing_user["password"]):
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="Invalid Username & Password")
    return {"message": "Login Successful."}