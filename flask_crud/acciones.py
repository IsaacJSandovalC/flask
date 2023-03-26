from conexion import collection
from flask import request, render_template, Flask, url_for, redirect
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
    data = [slang for slang in collection.find()]
    return render_template('index.html', items=data)


@app.route('/insertar', methods=['POST'])
def insertar():
    collection.insert_one({'palabra': request.form['palabra'], 
                           'descripcion': request.form['descripcion']})
    
    return redirect(url_for('inicio'))


@app.route('/editar', methods=['POST'])
def editar_valor():
    collection.update_one(
        {'_id': ObjectId(request.form['id'])},
        {'$set': {
            "palabra": request.form['palabra'],
            "significado": request.form['descripcion'],
        }})

    return redirect(url_for('inicio'))


@app.route('/eliminar', methods=['POST'])
def eliminar_valor():
    collection.delete_one({'_id': ObjectId(request.form['id'])})
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(port=5050, debug=True)
