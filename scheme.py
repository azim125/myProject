from pydantic import BaseModel
from datetime import date

class Usercreateshcema(BaseModel):
    username:str
    password:str
    height:float
    class Config:
        extra="forbid"
class New_weight(BaseModel):
    username:str
    weight:float
    date : date
    class Config:
        extra="forbid"
