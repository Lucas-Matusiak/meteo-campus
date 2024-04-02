import requests
from lxml import etree as ET
from datetime import datetime

lat = '44.34'
lon = '10.99'
api_key = 'a1b1045de421855d4d44bb2b53d4da8f'
def get_daily_weather(lat,lon,api_key):
    api_call = f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={7}&appid={api_key}&mode=xml&units=metric"
    response = requests.get(api_call)
    if response:
        xml_content = response.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(str(xml_content))

        forecast_data = []
        forecast_times = root.findall(".//time")

        for time in forecast_times:
            date_utc = time.get("day")
            temperature_max = round(float(time.find("temperature").get("max")))
            temperature_min = round(float(time.find("temperature").get("min")))
            wind_speed_mps = float(time.find("windSpeed").get("mps"))
            wind_speed_kmh = round(wind_speed_mps * 3.6)
            weather_description = time.find("symbol").get("name")

            day_data = {
                "date_utc": date_utc,
                "temperature_max": temperature_max,
                "temperature_min": temperature_min,
                "wind_speed_kmh": wind_speed_kmh,
                "weather_description": weather_description
            }
            forecast_data.append(day_data)

    return forecast_data


fr = get_daily_weather(lat, lon, api_key)
for day in fr:
    print(day)