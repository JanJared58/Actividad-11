import requests

def main():
    url = "https://swapi.dev/api/people/?page=1"
    
    response = requests.get(url)
    
    if response.status_code == 200:

        data = response.json()
        personajes = data.get("results", [])
        
        print("Personajes que comienzan con la letra 'L':")

        for personaje in personajes:
            
            nombre = personaje.get("name", "")
            if nombre.startswith("L"):
                altura = personaje.get("height", "Desconocida")
                print(f"Nombre: {nombre}, Altura: {altura} cm")
    else:
        print("Error al acceder a la API de Star Wars.")

if __name__ == "__main__":
    main()
