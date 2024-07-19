import models.usuarios_roles
import schemas.usuarios_roles
from sqlalchemy.orm import Session

def get_userrol(db: Session, id_user: int, id_rol: int):
    return db.query(models.usuarios_roles.UserRol).filter(models.usuarios_roles.UserRol.Usuario_ID == id_user, models.usuarios_roles.UserRol.Rol_ID== id_rol).first()

def get_usuarios_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.usuarios_roles.UserRol).offset(skip).limit(limit).all()

def create_userrol(db: Session, userrol: schemas.usuarios_roles.UserRolCreate):
    db_userrol = models.usuarios_roles.UserRol(Usuario_ID=userrol.Usuario_ID, 
                                          Rol_ID = userrol.Rol_ID,
                                          Estatus = userrol.Estatus, 
                                          Fecha_Registro = userrol.Fecha_Registro,
                                          Fecha_Actualizacion = userrol.Fecha_Actualizacion 
                                )
    db.add(db_userrol)
    db.commit()
    db.refresh(db_userrol)
    return db_userrol

def update_userrol(db: Session, id_user: int, id_rol: int, userrol: schemas.usuarios_roles.UserRolUpdate):
    db_userrol = db.query(models.usuarios_roles.UserRol).filter(models.usuarios_roles.UserRol.Usuario_ID == id_user,models.usuarios_roles.UserRol.Rol_ID == id_rol).first()
    if db_userrol:
        for var, value in vars(userrol).items():
            setattr(db_userrol, var, value) if value else None
        db.commit()
        db.refresh(db_userrol)
    return db_userrol

def delete_userrol(db: Session, id_user: int, id_rol:int):
    db_userrol = db.query(models.usuarios_roles.UserRol).filter(models.usuarios_roles.UserRol.Usuario_ID == id_user, models.usuarios_roles.UserRol.Rol_ID== id_rol).first()
    if db_userrol:
        db.delete(db_userrol)
        db.commit()
    return db_userrol