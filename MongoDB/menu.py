from conexion import conn, client
from acciones import Slangs

while True:
    print('--------------------------------------------------------------')
    print('Este es el menu de nuestra base de datos, ingresa tu accion:\n'
          '1. Agregar valor\n'
          '2. Actualizar valor\n'
          '3. Busca el significado \n'
          '4. Eliminar valor\n'
          '5. Imprimir todos los valores\n'
          '6. Salir'
          )
    desicion = input("Que deseas hacer?: ")

    if desicion == '1':
        print("\n*********** Insertar ***********")
        palabra = input("Nombre del slang: ")
        significado = input("Significado del slang: ")
        data = Slangs(palabra, significado)
        id = Slangs.insertar(data)
        print(f"El id del valor insertado es: {id}\n")

    elif desicion == '2':
        print("\n*********** Actualizar ***********")
        value = input("Ingresa el ID del slang que deseas cambiar: ")
        palabra = input("Nombre del nuevo slang: ")
        significado = input("Significado del slang: ")
        data = Slangs(palabra, significado)
        Slangs.actualizar(value, data)
        print("El slang se ha actualizado correctamente\n")
        
    elif desicion == '3':
        print("\n*********** Buscar ***********")
        value = input("Ingresa el ID del slang que deseas buscar: ")
        data = Slangs.buscar(value)
        print(f'El significado de "{data["palabra"]}" es: {data["significado"]}\n')
    
    elif desicion == '4':
        print("\n*********** Eliminar ***********")
        value = input("Ingresa el ID del slang que deseas eliminar: ")
        Slangs.eliminar(value)
        print("El slang se ha eliminado correctamente\n")
        
    elif desicion == '5':
        print('\n*********** Listado de slangs ***********')
        print(Slangs.mostrar_todos(),"\n")
        
    elif desicion == '6':
        print(f'\n*********** Gracias por usar el programa!! ***********')
        client.close()
        break