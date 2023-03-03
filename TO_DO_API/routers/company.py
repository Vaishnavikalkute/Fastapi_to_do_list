from fastapi import APIRouter,Depends
import schemas,model,crud,database
from sqlalchemy.orm import Session
from database import get_db
router=APIRouter(
    prefix="/company",
    tags=["company"]
)

@router.post("/")
async def create_company(cmp:schemas.company_create,db:Session=Depends(get_db)):
    db_cmp=crud.create_company(db,cmp)
    db.close()
    return db_cmp

#create user for company
@router.post("/user")
async def user_create(company_id:int,user:schemas.usercreate,db:Session = Depends(get_db)):
    fake_hashed_password = user.password + "notreallyhashed"
    dta = db.query(model.User).filter(model.User.email == user.email).first()
    if dta==None:
        db_user = model.User(company_id=company_id,email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        db.close()
        return db_user
    else:
        db.close()
        return {"response":f"this email '{user.email}' already exists"}

@router.get("/{company_id}",response_model=list[schemas.user_name])
async def get_user_id_by_company(company_id:int,db:Session=Depends(get_db)):
    db_user=db.query(model.User).filter(model.User.company_id==company_id).all()
    
    db.close()
 
    return db_user