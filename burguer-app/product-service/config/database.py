# Conecta ao banco de dados MongoDB utilizando as variáveis de ambiente

from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env

load_dotenv()

# Cria a conexão com o banco de dados MongoDB

client = MongoClient(
    os.getenv("MONGO_URI"),
    tlsCAFile=certifi.where()
)

# Seleciona o banco de dados
db = client["burguer_app_db"]

# função para retornar a instância do banco de dados
def get_db():
    return db
