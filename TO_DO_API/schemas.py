from typing import Optional
from pydantic import BaseModel

class ORMBase(BaseModel):
    class Config:
        orm_mode = True

class company_create(BaseModel):
    company_name:str


class user_name(BaseModel):
    email:str

    class Config:
        orm_mode = True

class usercreate(user_name):
     
     password:str

     

class company(company_create):
    id:int
    company_name:str
    user:list[usercreate]=[]

    class Config:
        orm_mode = True    

#complete todo schema
class ToDo(BaseModel):
    id:int
    task: str
    user_id:int

    class Config:
        orm_mode = True
    

#create todo schema
class todocreate(BaseModel):
    task: str


class user(usercreate):
    id=int
    tasks:list[ToDo]=[]

class user_temp(ORMBase):
    # id:Optional[int]
    # company_id:Optional[int]
    email:str

class Config:
        orm_mode = True


class login(BaseModel):
    username:str
    password:str









    