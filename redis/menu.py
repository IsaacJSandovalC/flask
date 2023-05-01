from conexion import conectar_redis
from acciones import crear_valor, leer_valor, actualizar_valor, eliminar_valor, mostrat_valores

# Menú principal
def menu():
    r = conectar_redis()
    
    while True:
        print("\n--- Menú CRUD de Redis ---")
        print("1. Crear valor")
        print("2. Leer valor")
        print("3. Actualizar valor")
        print("4. Eliminar valor")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_valor(r)
        elif opcion == "2":
            leer_valor(r)
        elif opcion == "3":
            actualizar_valor(r)
        elif opcion == "4":
            eliminar_valor(r)
        elif opcion == "5":
            mostrat_valores(r)
        elif opcion == "6":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida, seleccione de nuevo")

if __name__ == "__main__":
    menu()