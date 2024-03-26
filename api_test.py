import requests

def get_weather_data(latitude, longitude, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
    else:
        print("Erreur lors de la requête : ", response.status_code)
        return None

# Remplacez ces valeurs par vos propres coordonnées et votre clé API
latitude = "48.8566"
longitude = "2.3522"
api_key = "a1b1045de421855d4d44bb2b53d4da8f"

weather_data = get_weather_data(latitude, longitude, api_key)
if weather_data:
    print("Données météorologiques récupérées avec succès :")
    print(weather_data)
