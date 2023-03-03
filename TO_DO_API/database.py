from sqlalchemy import create_engine, Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

##The database.py file contains



# parameter inside create_engine() is the database url ,dialect+url
engine=create_engine("sqlite:///todo.db")

#sessionlocal()
sessionLocal= sessionmaker(bind=engine ,expire_on_commit=False)

#create declarative
Base=declarative_base()

#create a table inheriting from base


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()