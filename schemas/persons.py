from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

from models.persons import MyGenero, MySangre

class PersonBase(BaseModel):
    Titulo_Cortesia:str
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: str
    Curp: str
    Genero: MyGenero
    Sangre: MySangre
    Fecha_Nacimiento: datetime
    Fotografia:str
    Telefono: str
    Correo_Electronico: str
    Estatus:bool
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime

    
    
class PersonCreate(PersonBase):
    pass
class PersonUpdate(PersonBase):
    pass
class Person(PersonBase):
    ID:int
    #owner_id:int clave foranea
    
    class Config:
        orm_mode=True
        