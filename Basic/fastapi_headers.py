# Headers


from fastapi import FastAPI, Header
import nest_asyncio
nest_asyncio.apply()

app = FastAPI()

@app.get("/get_headers")
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    Host: str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["content_type"] = content_type
    request_headers["user_agent"] = user_agent
    request_headers["Host"] = Host

    return request_headers