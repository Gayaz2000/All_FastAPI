# FastAPI Auth

from sqlalchemy import Table, Column, Integer, String, MetaData

users = Table(
    "users",
    MetaData,
    Column("id", Integer, primary_= True),
    Column("user_name", String),
    Column("password", str)
)