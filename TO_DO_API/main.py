from fastapi import FastAPI , status ,Depends
from fastapi import HTTPException
from database import Base, engine,sessionLocal, get_db
from typing import List
import model ,database
import schemas

from sqlalchemy.orm import Session

from routers import user,authentication, company

from fastapi.middleware.cors import CORSMiddleware


#create the database
model.Base.metadata.create_all(engine)

#INSTANCE OF FASTAPI
app= FastAPI()

origins = [
   '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication.router)
app.include_router(company.router)
app.include_router(user.router)




@app.get("/")
async def root():
    return "To do list home"












    


















#create task
# response_model is a parameter of the "decorator" method (get, post, etc). 
#Not of your path operation function, like all the parameters and bod
#resposnse model creates object 
@app.post("/todo/", response_model=schemas.todocreate ,status_code=status.HTTP_201_CREATED)
async def create_todo(todo:schemas.todocreate, session:Session=Depends(get_db)):
    
    #create a session
    # session=Session(bind=engine, expire_on_commit=False)

 
    #create an instance of todo database model 
    tododb= model.ToDo(task=todo.task)
    #grab the id given to the object from the database
    session.add(tododb)
    session.commit()

    # session.refresh(tododb) after session.commit(). If you don’t refresh the session, 
    #the tododb object doesn’t get updated with the database-generated id.
    session.refresh(tododb)

    #get the id of task
    id=tododb.id

    session.close()
    print(id)
# only the response model data should be returned
    return todo

#get item as specified
@app.get("/todo/{id}",response_model=schemas.ToDo) 
async def read_todo(id: int):
    session= Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo=session.query(model.ToDo).get(id)

    session.close()

    #if the id is not present it should raise following exception
    if not todo:
        raise HTTPException(status_code=404, detail= f"todo item with id {id} not found")
    return todo

#update value of todo item by id
@app.put("/todo/{id}")
def update_todo(id: int,task:str):
    session=Session(bind=engine, expire_on_commit=False) 

    todo=session.query(model.ToDo).get(id)

    if todo:
        todo.task=task
        session.commit()
    
    session.close()
    if not todo:
         raise HTTPException(status_code=404,detail= f"todo item with id {id} not found")

    return f"update todo item with id {id} and {todo.task}"

#delete item by id


#read all the items
@app.get("/todo", response_model = List[schemas.ToDo])
def read_todo_list():
    session=Session(bind=engine,expire_on_commit=False)

    todo_list=session.query(model.ToDo).all()

    session.close()
    return todo_list



# if __name__=='__main__':
#     uvicorn.run(app,'0.0.0.0',port=8080,reload=True)