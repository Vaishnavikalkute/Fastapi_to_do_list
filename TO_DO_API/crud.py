from sqlalchemy.orm import Session

import model
import schemas


def create_company(db:Session,cmp:schemas.company_create):
     db_company=model.Company(company_name=cmp.company_name)
     db.add(db_company)
     db.commit()
     db.refresh(db_company)
     db.close()
     return db_company

def read_all_user(db:Session):
    db_user=db.query(model.User).all()
    print("####################",db_user[1])
    db.close()
    return db_user


def create_user_task(db:Session, task:schemas.todocreate,user_id_input:int):
    db_task=model.ToDo(task=task.task, user_id=user_id_input)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()

    return db_task

def read_items(db:Session,user_id:int):
    b=db.query(model.ToDo).filter(model.ToDo.user_id==user_id).all()
    db.close()
    return b