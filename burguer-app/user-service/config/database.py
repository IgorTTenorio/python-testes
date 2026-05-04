from pathlib import Path
import os

import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

client = MongoClient(
    os.getenv("MONGO_URI"),
    tlsCAFile=certifi.where()
)

# Seleciona o banco de dados
db = client["burguer_app_db"]

# função para retornar a instância do banco de dados
def get_db():
    return db
