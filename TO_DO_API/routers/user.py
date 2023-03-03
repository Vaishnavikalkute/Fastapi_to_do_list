from typing import List
from fastapi import APIRouter,HTTPException,status
from fastapi import Depends
import schemas
from database import engine
from database import get_db
import model
import crud
from sqlalchemy.orm import Session
import database


router=APIRouter(
    prefix="/company/{company_id}/user",
    tags=["User"]
)




@router.get("/",response_model=list[schemas.user_name])
async def get_user(db:Session=Depends(get_db)):
    db_user=db.query(model.User).all()
    # db_user=db.query(model.User).filter(model.User.company_id==company_id_)
    
    db.close()
    print("####################",db_user)
    return db_user


#create task for user
@router.post("/{user_id}/todo",response_model=schemas.ToDo)
async def create_task_for_user( company_id:int,user_id: int, task: schemas.todocreate, db:Session = Depends(get_db)):
    db_task= crud.create_user_task(db=db, task=task, user_id_input=user_id)
    db.close()
    return db_task


#get all the tasks
@router.get("/{user_id}/all_todos",response_model=list[schemas.ToDo])
async def get_item(user_id:int,db:Session=Depends(get_db)):

    a=crud.read_items(db,user_id)
    # print(schemas.ToDo)
    db.close()
    return a


@router.delete("/{user_id}/todo/{id}")
def delete_todo(id: int):
    session=Session(bind=engine, expire_on_commit=False)

    todo=session.query(model.ToDo).get(id)

    if todo:
        session.delete(todo)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail="The task id:{id} does not exist.")

    return f"Id:{id} deleted successfully"