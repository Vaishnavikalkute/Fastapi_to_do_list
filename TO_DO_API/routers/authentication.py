from ast import List
import json

from fastapi import APIRouter,Depends,HTTPException,status
import schemas , database ,model
from sqlalchemy.orm import Session
from database import get_db

router =APIRouter(
    tags=['Authentication']
)


@router.post('/login')
async def login(request:schemas.login, db:Session=Depends(get_db)):
    db_login=db.query(model.User).filter(model.User.email==request.username).first()
    # print(db_login)
    if db_login== None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credential")
        
    db.close()
    return db_login


