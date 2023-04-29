## Taller #3 Flask y MongDB<a name="id3"></a>
Este trabajo se emplea utilizando Python, pymongo y flask se crea una colecion llamada "flask" y un documento llamado "flask_mongo". 

Se le agregan las funciones de:

* Agregar nueva palabra.
* Editar palabra existente.
* Eliminar palabra existente.
* Ver listado de palabras.

para su uso correcto, reemplazar las credenciales del archivo [conexion.py](https://github.com/IsaacJSandovalC/flask/blob/main/flask_crud/conexion.py) por sus credenciales en MongoDB de la siguiente manera:

```
MONGODB_HOST = 'Host name'
MONGODB_PORT = 'Ussing port'
MONGODB_TIMEOUT = timer (colocar en enteros)
```
Posterior a estos ajustes, ejecutar el archivo llamado [acciones.py](https://github.com/IsaacJSandovalC/flask/blob/main/flask_crud/acciones.py), este creará automanticamente todas las colecciones y documentos con sus registros.

### Y listo!! que disfrute.
