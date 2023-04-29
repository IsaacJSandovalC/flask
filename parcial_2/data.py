# Implementamos la data en un API de tipo REST
<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask, jsonify
>>>>>>> main
import pandas as pd
import json

app = Flask(__name__)

# Lee los datos del archivo .xls
<<<<<<< HEAD
data = pd.read_excel('flask/parcial_2/data.xls', sheet_name='Data',  header=2)
=======
data = pd.read_excel('./parcial_2/data.xls', sheet_name='Data',  header=2)
>>>>>>> main
data.columns = data.iloc[0]
df = data.iloc[1:]

@app.route('/')
def index():
    panama_data = df[df['Country Name'] == 'Panama']
    json_data = panama_data.to_json(orient='records')
<<<<<<< HEAD
    data = json.loads(json_data)
    return render_template('index.html', data=data)

=======
    
    return jsonify(json_data)
>>>>>>> main

if __name__ == '__main__':
    app.run()
