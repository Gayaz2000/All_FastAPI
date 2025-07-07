# ORM --> Object Relational Mapper

from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine

engine = AsyncEngine(create_engine(
    url= Config.DATABASE_URL, # make a BaseSettings schema
    echo = True
))

async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT 'hello';")

        result = await conn.execute(statement)
        print(result.all())