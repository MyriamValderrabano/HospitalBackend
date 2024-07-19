from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyGenero(enum.Enum):
    Masculino="Masculino"
    Femenino="Femenino"
    Otro="Otro"

class MySangre(enum.Enum):
    AP="A+"
    AN="A-"
    BP="B+"
    BN="B-"
    ABP="AB+"
    OP="O+"
    OB="O-"



class Person(Base):
    __tablename__ = "tbb_personas"
    
    ID = Column(Integer, primary_key=True, index=True)
    Titulo_Cortesia= Column(String(255))
    Nombre = Column(String(255))
    Primer_Apellido = Column(String(255))
    Segundo_Apellido = Column(String(255))
    Curp = Column(String(18)) 
    Genero = Column(Enum(MyGenero))  
    Sangre = Column(Enum(MySangre))  
    Fecha_Nacimiento = Column(DateTime)
    Fotografia= Column(String(255))
    Telefono = Column(String(20)) 
    Correo_Electronico = Column(String(255))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion=Column(DateTime)
    