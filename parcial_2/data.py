# Implementamos la data en un API de tipo REST
from flask import Flask, render_template

import pandas as pd
import json

app = Flask(__name__)

# Lee los datos del archivo .xls
data = pd.read_excel('flask/parcial_2/data.xls', sheet_name='Data',  header=2)

data.columns = data.iloc[0]
df = data.iloc[1:]

@app.route('/')
def index():
    panama_data = df[df['Country Name'] == 'Panama']
    json_data = panama_data.to_json(orient='records')
    data = json.loads(json_data)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
