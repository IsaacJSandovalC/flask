import requests

def get_data(url):
    resp = requests.get(url)
    data = resp.json()
    return data

def get_section(url, section):
    result = url[section]
    data = get_data(result)
    return data

numbers = []
respuesta = get_data("https://swapi.dev/api/")
data_film = get_section(url=respuesta, section="films")