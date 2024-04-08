from fastapi import APIRouter, HTTPException
from models.RuleBot import RuleBot
from models.Mensaje import Message
from controllers.chat import ChatController
import spacy

# Cargar el modelo de lenguaje de spaCy
nlp = spacy.load("es_core_news_md")

chat = APIRouter()
rulebot = RuleBot()
chatController = ChatController()

@chat.get("/start")
async def start():
    response = chatController.startChat()
    return response

@chat.post("/chat")
async def ctrChat(prompt: Message):


    opciones = [
        "orientacion vocacional mas afin a mi",
        "carrera mas demandada",
        "informacion de las carreras ofertadas"
    ]

    mejor_similitud = 0
    mejor_indice = -1
    
    # Procesar la entrada del usuario
    doc_usuario = nlp(prompt.text)
    
    for i, opcion in enumerate(opciones):
        # Procesar la opción
        doc_opcion = nlp(opcion)
        
        # Calcular la similitud entre la entrada del usuario y la opción
        similitud = doc_usuario.similarity(doc_opcion)
        
        # Actualizar el mejor índice si se encuentra una similitud más alta
        if similitud > mejor_similitud:
            mejor_similitud = similitud
            mejor_indice = i
    
    # Devolver el índice de la mejor coincidencia
    return mejor_indice

    response = rulebot.match_reply(prompt.text)
    if not response:
        raise HTTPException(status_code=400, detail="Respuesta no encontrada")
    return {"response": str(response)}
