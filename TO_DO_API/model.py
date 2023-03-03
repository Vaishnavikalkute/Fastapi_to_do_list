from sqlalchemy import create_engine, Column,Integer,String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__='company'
    id= Column(Integer, primary_key=True)
    company_name=Column(String(50))
    company_user=relationship("User",back_populates="company")


class User(Base):
    __tablename__='company_user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String,unique=True)
    hashed_password = Column(String) 

    todos=relationship("ToDo", back_populates="user")
    
    company_id=Column(Integer,ForeignKey("company.id"))
    company=relationship("Company",back_populates="company_user")
    


class ToDo(Base):
    __tablename__='todos'
    id= Column(Integer, primary_key=True)
    task=Column(String(50))
    user_id=Column(Integer, ForeignKey("company_user.id"))

    user=relationship("User", back_populates="todos")



