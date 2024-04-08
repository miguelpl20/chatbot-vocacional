from fastapi import FastAPI
from routes.chat import chat

#INICIAR LA APLICACION
app = FastAPI()

#INCLUIR LAS RUTAS
app.include_router(chat)

