from fastapi_signals import signal
from fastapi import FastAPI,Request,HTTPException
from .db import db
from .config import SECRET_KEY
import jwt

api = FastAPI()
@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get("/ids/{count}")
def main(req:Request,count:int):
    token = req.headers["Authorization"].split()[1]
    if token is not signal:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
            )
    else:
        print(token)
    s = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    print(s)
    return db.list(count)


@api.get("/image/{id}")
def image(id:int):
    return db.image(id)