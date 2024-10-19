from models import *
from scheme import *
from sqlalchemy.orm import Session
from exceptions import *
from setting  import DATABASE_URL
import bcrypt
def create_user_in_db(data:Usercreateshcema,db:Session):
    hashed_password=bcrypt.hashpw(data.password.encode("utf-8"),bcrypt.gensalt())
    new_user=User(username=data.username,password=hashed_password.decode("utf-8"),height=data.height)
    user=db.query(User).filter_by(username=new_user.username).first()
    if user:
        raise UserIsExists()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"new user is created"} 
def add_your_weight(*,data:New_weight,db:Session):
    user=db.query(User).filter_by(username=data.username).first()
    user_weight=db.query(Weight).filter_by(username=data.username,date=data.date).first()
    new_weight_of_user=Weight(username=data.username,weight=data.weight,date=data.date)
    if not user:
        raise UserNotFoundException()
    if user_weight:
        db.query(Weight).filter_by(username=data.username,date=data.date).update({"weight":data.weight})
        db.commit()
        return {"msg":"weight is added"}
    db.add(new_weight_of_user)
    db.commit()
    db.refresh(new_weight_of_user)
    return {"msg":" new weight is added"}
     
def last_weight(*,username: str, db: Session):
    user = db.query(User).filter_by(username=username).first()  # Fixed this line
    if not user:
        raise UserNotFoundException()
    get_last_weight = db.query(Weight).filter(Weight.username == username).order_by(Weight.date.desc()).first()
    if not get_last_weight:
        raise DetailNotFound()
    return get_last_weight.weight
def changing_weight(*,username:str,db:Session):
    firstWeight=db.query(Weight).filter(Weight.username == username).order_by(Weight.date.asc()).first()
    latestWeight=db.query(Weight).filter(Weight.username == username).order_by(Weight.date.desc()).first()
    print(firstWeight)
    if firstWeight and latestWeight:
        weight_change = latestWeight.weight - firstWeight.weight # Extract the numerical values
        return {"weight_change": weight_change}
    raise DetailNotFound()

def calculated_bmi(*,username: str, db: Session):
    user1 = db.query(User).filter_by(username=username).first()
    latest_weight = last_weight(username=username,db=db)
    if user1 and latest_weight:
        height_in_meters = user1.height / 100  
        bmi = latest_weight / (height_in_meters ** 2)
        return bmi
    raise DetailNotFound()