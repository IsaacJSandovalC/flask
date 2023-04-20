from conexion import get_data, get_section, data_film, numbers

for result in data_film["results"]:
    planets = result["planets"]

    for planet in planets:
        request = get_data(planet)

        if request["climate"] == "arid":
            print(f"{result['title']} - {request['name']}")

for result in data_film["results"][5]["species"]:
    request = get_data(result)
    total_wookies = request["name"].count("Wookie") + 1

    if request["name"] == "Wookie":
        print(f"En la pelicula {data_film['results'][5]['title']} hay {total_wookies} Wookies")

for result in data_film["results"]:
    starships = result["starships"]
    
    for starship in starships:
        request = get_data(starship)
        length = request["length"]
        name = request["name"]

        cleaned_number = ''.join(c for c in length if c.isdigit() or c == '.')        
        numbers.append((float(cleaned_number), name))
        
max_number, name = max(numbers)
print(f"La nave con el número más grande es {name} con una longitud de {max_number}") 

