import redis

# Función para conectarse a Redis
def conectar_redis():
    r = redis.Redis(host='localhost', port=6379, db=0)
        
    slangs = [
        {"palabra": "que xopa", "significado": "expresion utilizada para saludar"},
        {"palabra": "yalabetia", "significado": "accion y efecto de sorpresa"},
        {"palabra": "chantin", "significado": "referencia al domicilio de alguna persona"},
        {"palabra": "fren", "significado": "haciendo referencia a algun amigo o conocido"},
        {"palabra": "lapesillo","significado": "haciendo referencia a que la persona es un joven"}]
    
    # Insertar cada par clave-valor en Redis
    for palabra in slangs:
        r.set(palabra['palabra'], palabra['significado'])
        
    return r

