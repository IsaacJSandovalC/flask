from conexion import collection

slangs = [
    {"palabra": "que xopa", "significado": "expresion utilizada para saludar"},
    {"palabra": "yalabetia", "significado": "accion y efecto de sorpresa"},
    {"palabra": "chantin", "significado": "referencia al domicilio de alguna persona"},
    {"palabra": "fren", "significado": "haciendo referencia a algun amigo o conocido"},
    {"palabra": "lapesillo","significado": "haciendo referencia a que la persona es un joven"}
]

palabra = collection.distinct("palabra")
new_slangs = [slang for slang in slangs if slang["palabra"] not in palabra]

if new_slangs:
    res = collection.insert_many(new_slangs)

