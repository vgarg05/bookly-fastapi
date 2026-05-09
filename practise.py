from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get('/greet')
async def greet(marks: int, name: Optional[str] = None) -> dict:

    return {"message": f"Hello, {name}!", "marks": marks}


class BookCreateModel(BaseModel):
     title:str
     author:str
         
@app.post('/create_book')
async def create_book(book_data: BookCreateModel) :
    return {
        "title":book_data.title,
        "author":book_data.author
    }


@app.get("/get_headers",status_code=500)
async def get_headers(
    accept:str=Header(None),
    content_type:str=Header(None),
    user_agent:str=Header(None),
    host:str=Header(None)
    ):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"]=host
    return request_headers
     
    postgresql://neondb_owner:npg_ajwmh6Zxz8sv@ep-little-night-aqafl6es-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require