from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hellow world."}

class InputData(BaseModel):
    mensagem: str

@app.post("/input/")
async def collect_input(data: InputData):
    # Imprime o conteúdo da entrada no terminal
    print(f"Conteúdo recebido: {data.mensagem}")
    
    # Retorna o conteúdo recebido como resposta
    return {"retorno": data.mensagem}