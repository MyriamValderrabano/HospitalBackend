from typing import Optional
from fastapi import HTTPException,Request,Depends
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jwt_config import valida_token
import crud.users, config.db, models.users

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db=config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class Portador(HTTPBearer):
    async def __call__(self, request: Request, db:Session=Depends(get_db)):
        autorizacion=await super().__call__(request)
        dato=valida_token(autorizacion.credentials)
        db_userLgin=crud.users.get_user_by_credentials(db,usuario=dato["Nombre_Usuario"],Correo_Electronico=dato["Correo_Electronico"],Telefono=dato["Numero_Telefonico_Movil"], password=dato["Contrasena"])
        if db_userLgin is None:
            raise HTTPException(status_code=404, detail="Login Incorrecto")
        print(db_userLgin)
        return db_userLgin