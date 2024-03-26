import requests

def get_coordinate(local):
    url = f"https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-implantations_etablissements_d_enseignement_superieur_publics/records?select=siege_lib%2Cimplantation_lib%2Clocalisation%2Ccoordonnees&where=localisation%20like%20%22Bordeaux%22&limit=100"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erreur lors de la requête : ", response.status_code)
        return None

local = "Bordeaux"
coordinate = get_coordinate(local)
if coordinate:
    #print(coordinate)
    total_count = coordinate["total_count"]
    results = coordinate["results"]

    # Parcourir les résultats
    for result in results:
        siege_lib = result["siege_lib"]
        implantation_lib = result["implantation_lib"]
        localisation = ", ".join(result["localisation"])
        coordonnees = result["coordonnees"]

        # Afficher les informations
        """print(f"Nom de l'établissement: {siege_lib}")
        print(f"Implantation: {implantation_lib}")
        print(f"Localisation: {localisation}")
        print(f"Coordonnées géographiques (lon, lat): {coordonnees['lon']}, {coordonnees['lat']}")
        print()"""

print(results[0]["coordonnees"])

def get_weather_data(latitude, longitude, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erreur lors de la requête : ", response.status_code)
        return None

# Remplacez ces valeurs par vos propres coordonnées et votre clé API
latitude = results[0]["coordonnees"]["lat"]
longitude = results[0]["coordonnees"]["lon"]
api_key = "a1b1045de421855d4d44bb2b53d4da8f"

weather_data = get_weather_data(latitude, longitude, api_key)
if weather_data:
    print("Données météorologiques récupérées avec succès :")
    print(weather_data)