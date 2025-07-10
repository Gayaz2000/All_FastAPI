from fastapi import FastAPI
from Configs.config import settings

app = FastAPI()
print(settings.database_url)

@app.get("/")
async def get_root():
    return {"messages": "Loaded Env Variables"}