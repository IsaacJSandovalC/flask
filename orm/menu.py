from slangs import Slangs
from conexion import Sesion, engine, Base

Base.metadata.create_all(engine)

session = Sesion()
Slangs.insert_slangs(session)

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
        new_slang = Slangs(nombre=palabra, definicion=significado)
        session.add(new_slang)
        session.commit()

    elif desicion == '2':
        value = input("Ingresa el ID que deseas cambiar: ")
        update_slang = session.query(Slangs).filter(Slangs.id == value).first()

        update_slang.nombre = input("Ingresa la palabra nueva: ")
        update_slang.definicion = input("Ingresa el significado nuevo: ")
    
        session.commit()


    elif desicion == '3':
        palabra = input("Ingresa la palabra que deseas buscar: ")
        result = session.query(Slangs).filter(Slangs.nombre == palabra).first()

        if result:
            significado = result.definicion
            print(f'resultado:\n{significado}')
        else:
            print("La palabra no fue encontrada en la tabla.")


    elif desicion == '4':
        value = input("Ingresa el ID que deseas borrar: ")
        slang_to_delete = session.query(Slangs).filter(Slangs.id == int(value)).first()
        if slang_to_delete:
            session.delete(slang_to_delete)
            session.commit()
        else:
            print("La palabra no se encuentra en la tabla.")

    elif desicion == '5':
        slangs = session.query(Slangs).all()
        for slang in slangs:
            print(f'Id: {slang.id}, Palabra: {slang.nombre}, Significado: {slang.definicion}')

    elif desicion == '6':
        print(f'Gracias por usar el programa!!')
        session.commit()
        session.close()
        break



