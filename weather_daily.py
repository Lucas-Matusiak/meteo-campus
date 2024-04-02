
import requests
from lxml import etree as ET
from datetime import datetime

lat = '47.7279751376'
lon = '7.30700846528'
api_key = 'a1b1045de421855d4d44bb2b53d4da8f'
def get_current_weather(lat, lon, api_key):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + api_key + "&units=metric&mode=xml&lang=fr")
    if response:
        # print(response.text)

        xml_content = response.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(str(xml_content))

        # Accessing elements
        city_name = root.find('city').attrib['name']
        temperature_value = round(float(root.find('temperature').attrib['value']))
        temperature_unit = "°c"#root.find('temperature').attrib['unit']
        humidity_value = root.find('humidity').attrib['value']
        humidity_unit = root.find('humidity').attrib['unit']
        feels_like_value =round(float(root.find('feels_like').attrib['value']))
        feels_like_unit = "°c"
        wind_speed = round(3.6 * float(root.find('wind/speed').attrib['value']))
        wind_speed_unit = "km/h"
        clouds_value = root.find('clouds').attrib['value']
        clouds_unit = "%"
        clouds_name = root.find('clouds').attrib['name']
        sun_rise_datetime = datetime.strptime(root.find('city/sun').attrib['rise'], '%Y-%m-%dT%H:%M:%S')
        sun_set_datetime = datetime.strptime(root.find('city/sun').attrib['set'], '%Y-%m-%dT%H:%M:%S')
        sun_rise = sun_rise_datetime.strftime('%H:%M')
        sun_set = sun_set_datetime.strftime('%H:%M')

        #last_update_value = root.find('lastupdate').attrib['value']
        #wind_speed_name = root.find('wind/speed').attrib['name']
        #wind_direction_value = root.find('wind/direction').attrib['value']
        #wind_direction_code = root.find('wind/direction').attrib['code']
        #wind_direction_name = root.find('wind/direction').attrib['name']
        #pressure_value = root.find('pressure').attrib['value']
        #pressure_unit = root.find('pressure').attrib['unit']
        #visibility_value = root.find('visibility').attrib['value']
        print ( city_name, temperature_value, temperature_unit,"humidité :",humidity_value, humidity_unit,"vitesse du vent :",wind_speed,wind_speed_unit,"precipitation :",clouds_value,clouds_unit,clouds_name,"lever du soleil",sun_rise,"coucher du soleil",sun_set
              )

        return {
            "city_name": city_name,
            "temperature_value": temperature_value,
            "temperature_unit": temperature_unit,
            "feels_like_value": feels_like_value,
            "feels_like_unit": feels_like_unit,
            "humidity_value": humidity_value,
            "humidity_unit": humidity_unit,
            "wind_speed": wind_speed,
            "wind_speed_unit": wind_speed_unit,
            "clouds_value": clouds_value,
            "clouds_unit": clouds_unit,
            "clouds_name": clouds_name,
            "sun_rise": str(sun_rise),
            "sun_set": str(sun_set)
        }

    else:
        raise Exception(f"Non-success status code: {response.status_code}")

# Printing values
get_current_weather(lat, lon, api_key)