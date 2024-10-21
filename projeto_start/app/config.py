import os
from motor.motor_asyncio import AsyncIOMotorClient

# Pegue a URI do MongoDB da variável de ambiente
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/meubanco")

client = AsyncIOMotorClient(MONGO_URI)
db = client["meubanco"]
