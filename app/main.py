
from fastapi import FastAPI
from .db import db
api = FastAPI()

@api.get("/")
async def root():
    return {"message": "Hello World"}

#@api.exception_handler(ValueError)
@api.get("/ids/{count}")
def main(count:int):
    return db.list(count)


@api.get("/image/{id}")
def image(id:int):
    return db.image(id)