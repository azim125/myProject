from fastapi import FastAPI,Depends
from db import get_db
from sqlalchemy.orm import Session
from scheme import Usercreateshcema
from service import *
app = FastAPI()


@app.get("/")
def healthy_check():
    return {"msg":"this is my site"}

@app.post("/user")
def creat_user(item: Usercreateshcema,db:Session=Depends(get_db)):
    message=create_user_in_db(data=item,db=db)
    return message

@app.post("/creat_weight")
def creat_user(item: New_weight,db:Session=Depends(get_db)):
    message=add_your_weight(data=item,db=db)
    return message   
@app.get("/getWeight")
def get_weight(username: str, db: Session = Depends(get_db)):
    message = last_weight(username=username, db=db)
    return message
@app.get("/changed_weight")
def changed_weight(username: str, db: Session = Depends(get_db)):
    message = changing_weight(username=username, db=db)
    return message
@app.get("/bmi")
def get_bmi(username: str, db: Session = Depends(get_db)):
    bmi = calculated_bmi( username=username,db=db)
    return {"bmi": bmi}