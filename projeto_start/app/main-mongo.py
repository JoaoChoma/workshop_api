from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId

app = FastAPI()

# Configurando a conexão com o MongoDB
client = AsyncIOMotorClient("mongodb://mongo:27017")
db = client["meu_banco"]  # Nome do banco de dados

@app.get("/")
def read_root():
    return {"message": "Hellow world."}

class Item(BaseModel):
    name: str
    description: str
    price: float


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()  # Converte para dicionário
    result = await db["items"].insert_one(item_dict)  # Insere o item no banco
    if result.inserted_id:
        return {"message": "Item inserido com sucesso", "id": str(result.inserted_id)}
    raise HTTPException(status_code=500, detail="Erro ao inserir o item")

@app.get("/items/")
async def get_items():
    items_cursor = db["items"].find()
    items = await items_cursor.to_list(length=100)  # Limite de 100 itens para a consulta
    for item in items:
        item["_id"] = str(item["_id"])  # Convertendo ObjectId para string
    return items