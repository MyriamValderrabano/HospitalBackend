# from fastapi import APIRouter
# from pydantic import BaseModel
# from datetime import datetime
# from typing import Optional

# persona= APIRouter()
# personas=[]
# class model_personas(BaseModel):
#     id:int
#     nombre:str
#     primer_apellido: str
#     segundo_apellido:Optional[str] 
#     edad:int
#     fecha_nacimiento:datetime
#     curp:str
#     tipo_sangre:str
#     created_at:datetime = datetime.now()
#     estatus: bool = False



# @persona.get('/')
# def bienvenida():
#     return "Bienvenido al api del sistema"

# @persona.get("/personas")
# def get_personas():
#     return personas

# @persona.post("/personas")
# def savePersonas(datos_persona:model_personas):
#     personas.append(datos_persona)
#     return "Datos guardados correctamente"


# @persona.put("/personas/{persona_id}")
# def updatePersonas(persona_id: int, datos_persona: model_personas):
#     for index, persona in enumerate(personas):
#         if persona.id == persona_id:
#             # Actualizar solo los campos modificables
#             persona.nombre = datos_persona.nombre
#             persona.primer_apellido = datos_persona.primer_apellido
#             persona.segundo_apellido = datos_persona.segundo_apellido
#             persona.edad = datos_persona.edad
#             persona.fecha_nacimiento = datos_persona.fecha_nacimiento
#             persona.curp = datos_persona.curp
#             persona.tipo_sangre = datos_persona.tipo_sangre
#             persona.created_at = datos_persona.created_at
#             persona.estatus = datos_persona.estatus
#             return "Datos actualizados correctamente"

# @persona.delete("/personas/{persona_id}")
# def deletePersonas(persona_id: int):
#     for index, persona in enumerate(personas):
#         if persona.id == persona_id:
#             del personas[index]
#             return "Datos eliminados correctamente"

# @persona.get("/personas/{persona_id}")
# def searchPersonas(persona_id: int):
#     for persona in personas:
#         if persona.id == persona_id:
#             return persona
