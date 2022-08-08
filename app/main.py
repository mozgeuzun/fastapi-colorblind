
from fastapi import FastAPI
from .db import db
api = FastAPI()

@api.get("/")
async def root():
    return {"message": "Hello World"}

3#@api.exception_handler(ValueError)
@api.get("/ids/{count}")
def main(count:int):
    return db.list(count)