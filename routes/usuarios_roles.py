from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
import crud.usuarios_roles, config.db, schemas.usuarios_roles, models.usuarios_roles
from portadortoken import Portador

from typing import List

userrol = APIRouter()

models.usuarios_roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@userrol.get("/usuarios_roles/", response_model=List[schemas.usuarios_roles.UserRol], tags=["Usuarios Roles"],dependencies=[Depends(Portador())])
def read_usuarios_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_usuarios_roles= crud.usuarios_roles.get_usuarios_roles(db=db, skip=skip, limit=limit)
    return db_usuarios_roles

@userrol.post("/userrol/{id_user}/{id_rol}", response_model=schemas.usuarios_roles.UserRol, tags=["Usuarios Roles"],dependencies=[Depends(Portador())])
def read_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol= crud.usuarios_roles.get_userrol(db=db, id_user=id_user,id_rol=id_rol)

    if db_userrol is None:
        raise HTTPException(status_code=404, detail="UserRol no existe")
    return db_userrol
    order = db.query(Order).filter(Order.order_id == order_id, Order.product_id == product_id).first()


@userrol.post("/userrols/", response_model=schemas.usuarios_roles.UserRol, tags=["Usuarios Roles"])
def create_user(userrol: schemas.usuarios_roles.UserRolCreate, db: Session = Depends(get_db)):
    db_userrol = crud.usuarios_roles.get_userrol(db=db, id_user=userrol.Usuario_ID, id_rol=userrol.Rol_ID)
    print (db_userrol)
    if db_userrol:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.usuarios_roles.create_userrol(db=db, userrol=userrol)

@userrol.put("/userrol/{id_user}/{id_rol}", response_model=schemas.usuarios_roles.UserRol, tags=["Usuarios Roles"],dependencies=[Depends(Portador())])
def update_user(id_user: int, id_rol: int, userrol: schemas.usuarios_roles.UserRolUpdate, db: Session = Depends(get_db)):
    db_userrol = crud.usuarios_roles.update_userrol(db=db, id_user=id_user, id_rol=id_rol, userrol=userrol)
    print (db_userrol.Estatus)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_userrol

@userrol.delete("/userrol/{id_user}/{id_rol}", response_model=schemas.usuarios_roles.UserRol, tags=["Usuarios Roles"],dependencies=[Depends(Portador())])
def delete_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol = crud.usuarios_roles.delete_userrol(db=db, id_user=id_user, id_rol=id_rol)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_userrol