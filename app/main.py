
'''
 Sistema de monitoramento de dispositivos conectados a rede da fábrica.
 Objetivo Monitoramento, verificar dispositivos ligados e desligados.
Identificar dispositivos ligados a rede dados de cada dispositivo(ID, MAC, NOME, SO).
Scan de vulnerabilidades dos dispositivos. Em especial os IIoT
'''

from fastapi import FastAPI
from app.routes.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware

#Iniciar a Aplicação
app = FastAPI()

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API em funcionamento!!"}

