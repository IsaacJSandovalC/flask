
# Funciones CRUD
def crear_valor(r):
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    r.set(clave, valor)
    print("Valor creado en Redis")

def leer_valor(r):
    clave = input("Ingrese la clave: ")
    valor = r.get(clave)
    if valor is not None:
        print(f"El valor para la clave {clave} es: {valor.decode('utf-8')}")
    else:
        print(f"No se encontró un valor para la clave {clave}")

def actualizar_valor(r):
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el nuevo valor: ")
    r.set(clave, valor)
    print("Valor actualizado en Redis")

def eliminar_valor(r):
    clave = input("Ingrese la clave: ")
    r.delete(clave)
    print("Valor eliminado de Redis")
    
def listar_valores(r):
    claves = r.keys()
    for clave in claves:
        valor = r.get(clave)
        print(clave.decode('utf-8'), valor.decode('utf-8'))

