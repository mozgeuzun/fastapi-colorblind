
from fastapi import FastAPI,Request
from .db import db
import jwt
SECRET_KEY='123456789'
api = FastAPI()
@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get("/ids/{rnd}")
def main(req:Request,rnd:int):
    token = req.headers["Authorization"].split()[1]
    try:
        s = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        print(s)
        return db.list(rnd)    
    except:
        a="ERROR!!"
        return a

   
    

@api.get("/image/{id}")
def image(id:int):
    return db.image(id)