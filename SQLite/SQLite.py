import sqlite3


def add_slang(text, word):
    cur.execute("INSERT INTO slangs (palabra, significado) VALUES (?, ?)",(palabra, significado))
    bd.commit()

def update_slang(value, text, word):
    cur.execute("UPDATE slangs SET palabra=?, significado=? WHERE id=?",(palabra, significado, int(value)))
    bd.commit()

def search_slang(text):
    cur.execute("SELECT significado FROM slangs WHERE palabra=?", (palabra,))
    result = cur.fetchone()
    return result[0] if result else None

def delete_slang(value):
    cur.execute("DELETE FROM slangs WHERE id=?", (int(value),))
    bd.commit()

def print_all_data():
    cur.execute("SELECT * FROM slangs")
    result = cur.fetchall()
    for row in result:
        print(row)
try:
    bd = sqlite3.connect('slangs.db')
    cur = bd.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS slangs (
            id INTEGER PRIMARY KEY,
            palabra TEXT,
            significado TEXT)
        """)

    slangs = {
        1: {"palabra": "que xopa", "significado": "expresión utilizada para saludar"},
        2: {"palabra": "yalabetia", "significado": "accion y efecto de sorpresa"},
        3: {"palabra": "chantin", "significado": "referencia al domicilio de alguna persona"},
        4: {"palabra": "fren", "significado": "haciendo referencia a algun amigo o conocido"},
        5: {"palabra": "lapesillo", "significado": "haciendo referencia a que la persona es un joven"}
    }

    for slang in slangs.values():
        cur.execute("SELECT * FROM slangs WHERE palabra=?", (slang["palabra"],))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO slangs (palabra, significado) VALUES (?, ?)",
                        (slang["palabra"], slang["significado"]))

    bd.commit()
    valor = True

    while valor:
        print('--------------------------------------------------------------')
        print('Este es el menu de nuestrA base de datos, ingresa tu accion:\n'
              '1. Agregar valor\n'
              '2. Actualizar valor\n'
              '3. Busca el significado \n'
              '4. Eliminar valor\n'
              '5. Imprimir todos los valores\n'
              '6. Salir'
              )

        desicion = input("Que deseas hacer?: ")

        if desicion == '1':
            palabra = input("Ingresa la palabra: ")
            significado = input("Ingresa el significado: ")
            add_slang(word=palabra, text=significado)

        elif desicion == '2':
            value = input("Ingresa el ID que deseas cambiar: ")
            palabra = input("Ingresa la palabra nueva: ")
            significado = input("Ingresa el significado nuevo: ")
            update_slang(value=value, text=significado, word=palabra)

        elif desicion == '3':
            palabra = input("Ingresa la palabra que deseas buscar: ")
            print(f'resultado:\n{search_slang(text=palabra)}')

        elif desicion == '4':
            value = input("Ingresa el ID que deseas borrar: ")
            delete_slang(value=value)

        elif desicion == '5':
            print_all_data()

        elif desicion == '6':
            print(f'Gracias por usar el programa!!')
            valor = False
            bd.close()
except:
    print(f'Error')