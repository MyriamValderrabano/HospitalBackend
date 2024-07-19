from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from portadortoken import Portador
import crud.users,config.db,schemas.users,models.users
from typing import List
from jwt_config import solicita_token

user = APIRouter()

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@user.get("/users/", response_model=List[schemas.users.User], tags=["Usuarios"], dependencies=[Depends(Portador())])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users= crud.users.get_users(db=db, skip=skip, limit=limit)
    return db_users

@user.post("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"],dependencies=[Depends(Portador())])
def read_user(id: int, db: Session = Depends(get_db)):
    db_user= crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/users/", response_model=schemas.users.User, tags=["Usuarios"])
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.users.get_user_by_usuario(db, usuario=user.Nombre_Usuario)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.users.create_user(db=db, user=user)

@user.put("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"],dependencies=[Depends(Portador())])
def update_user(id: int, user: schemas.users.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.users.update_user(db=db, id=id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_user

@user.delete("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"],dependencies=[Depends(Portador())])
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.users.delete_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_user

@user.post("/login/", response_model=schemas.users.User, tags=["Usuario Login"])
def read_credentials(user:schemas.users.UserLogin,db: Session = Depends(get_db)):
    db_credentials = crud.users.get_user_by_credentials(db,usuario=user.Nombre_Usuario,Correo_Electronico=user.Correo_Electronico,Telefono=user.Numero_Telefonico_Movil,password=user.Contrasena)
    if db_credentials is None:
        return JSONResponse(content={'mensaje':'Acceso Denegado'}, status_code=404)
    token: str = solicita_token(user.dict())
    return  JSONResponse(status_code=200, content= token)
    
