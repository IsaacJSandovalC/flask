from pymongo import MongoClient

# Configuración de la conexión a la base de datos de MongoDB
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = '27017'
MONGODB_TIMEOUT = 1000

URI_CONNECTION = f"mongodb://{MONGODB_HOST}:{MONGODB_PORT}/"

try:
    client = MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=MONGODB_TIMEOUT)
    print(f'OK -- Connected to MongoDB at server {MONGODB_HOST}\n')
    db = client["Slangs_db"]
    conn = db["Slangs"]

    
except Exception:
    print(f'Err -- no se pudo conectar con la base de datos de mongoDB')
    
    