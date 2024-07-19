from fastapi import FastAPI;
#from routes.persona import persona
#from routes.usuario import usuario

from routes.users import user
from routes.persons import person
from routes.roles import rol
from routes.usuarios_roles import userrol

app=FastAPI();
#app.include_router(persona)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)



print("Bienvenido a mi Aplicacion")