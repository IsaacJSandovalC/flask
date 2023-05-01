from conexion import conn
from bson.objectid import ObjectId

class Slangs:
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado

    def insertar(value):
        return conn.insert_one({
            "palabra": value.palabra,
            "significado": value.significado,
        }).inserted_id
        
    def actualizar(id, value):
        return conn.update_one(
            {'_id': ObjectId(id)}, 
                {'$set': {
                    "palabra": value.palabra,
                    "significado": value.significado,
                }})
        
    def buscar(id):
        return conn.find_one({'_id': ObjectId(id)})

    def eliminar(id):
        return conn.delete_one({'_id': ObjectId(id)})
    
    def mostrar_todos():
        data = [slang for slang in conn.find()]
        return f'\n'.join([f'{slang["palabra"]} - {slang["significado"]}' for slang in data])