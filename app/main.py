from fastapi import FastAPI,Request,HTTPException
from .db import db
import jwt
SECRET_KEY='123456789'
api = FastAPI()
@api.get("/")
async def root():
    return {"message": "Hello World"}

def clientValidate(req:Request):
    if "authorization" in req.headers.keys():
        jwt_header = req.headers["authorization"]
        arr = jwt_header.split(" ")
        if arr[0].lower() == "bearer" and len(arr)==2:
            try:
                return jwt.decode(arr[1], SECRET_KEY, algorithms=["HS256"])
            except:
                raise HTTPException(status_code=400,detail="Token is invalid")
        else:
            raise HTTPException(status_code=400,detail="'Authorization' header must be formatted as 'Bearer <token>'")
    else:
        raise HTTPException(status_code=400,detail="Authorization not sent")

@api.get("/ids/{rnd}")
def main(req:Request,rnd:int):
    clientInfo = clientValidate(req)
    print(clientInfo)
    return db.list(rnd)
   
@api.get("/image/{id}")
def image(id:int):
    return db.image(id)