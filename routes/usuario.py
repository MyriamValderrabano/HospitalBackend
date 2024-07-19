# from fastapi import APIRouter
# from pydantic import BaseModel
# from datetime import datetime
# from typing import Optional

# usuario= APIRouter()
# usuarios=[]
# class model_usuarios(BaseModel):
#     id:int
#     usuario:str
#     contrasena: str
#     persona_ID:int
#     created_at:datetime = datetime.now()
#     estatus: bool = False


# @usuario.get("/usuarios")
# def get_usuarios():
#     return usuarios

# @usuario.post("/usuarios")
# def saveUsuarios(datos_usuario:model_usuarios):
#     usuarios.append(datos_usuario)
#     return "Datos guardados correctamente"

# @usuario.put("/usuarios/{usuario_id}")
# def updateUsuarios(usuario_id: int, datos_usuario: model_usuarios):
#     for index, usuario in enumerate(usuarios):
#         if usuario.id == usuario_id:
#             # Actualizar solo los campos modificables
#             usuario.usuario = datos_usuario.usuario
#             usuario.contrasena = datos_usuario.contrasena
#             usuario.persona_ID = datos_usuario.persona_ID
#             usuario.estatus = datos_usuario.estatus
#             usuario.created_at = datos_usuario.created_at
#             return "Datos actualizados correctamente"
        

# @usuario.delete("/usuarios/{usuario_id}")
# def deleteUsuarios(usuario_id: int):
#     for index, usuario in enumerate(usuarios):
#         if usuario.id == usuario_id:
#             del usuarios[index]
#             return "Datos eliminados correctamente"
        
        

# @usuario.get("/usuarios/{usuario_id}")
# def searchUsuarios(usuario_id: int):
#     for usuario in usuarios:
#         if usuario.id == usuario_id:
#             return usuario
