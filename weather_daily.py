
import requests
from lxml import etree as ET
from datetime import datetime

lat = '44.34'
lon = '10.99'
api_key = 'a1b1045de421855d4d44bb2b53d4da8f'
def get_current_weather(lat, lon, api_key):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + api_key + "&units=metric&mode=xml")
    if response:
        # print(response.text)

        xml_content = response.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(str(xml_content))

        # Accessing elements
        city_name = root.find('city').attrib['name']
        temperature_value = round(float(root.find('temperature').attrib['value']))
        temperature_unit = root.find('temperature').attrib['unit']
        humidity_value = root.find('humidity').attrib['value']
        humidity_unit = root.find('humidity').attrib['unit']
        pressure_value = root.find('pressure').attrib['value']
        pressure_unit = root.find('pressure').attrib['unit']
        wind_speed = round(3.6 * float(root.find('wind/speed').attrib['value']))
        wind_speed_unit = root.find('wind/speed').attrib['unit']
        wind_speed_name = root.find('wind/speed').attrib['name']
        wind_direction_value = root.find('wind/direction').attrib['value']
        wind_direction_code = root.find('wind/direction').attrib['code']
        wind_direction_name = root.find('wind/direction').attrib['name']
        clouds_value = root.find('clouds').attrib['value']
        clouds_name = root.find('clouds').attrib['name']
        visibility_value = root.find('visibility').attrib['value']
        last_update_value = root.find('lastupdate').attrib['value']

        print(wind_speed)
        # return {city_name, temperature_value, temperature_unit, humidity_value, humidity_unit, pressure_value, pressure_unit,
        #     wind_speed, }
    else:
        raise Exception(f"Non-success status code: {response.status_code}")

# Printing values
get_current_weather(lat, lon, api_key)