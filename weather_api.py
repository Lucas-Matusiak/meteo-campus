
import requests
from lxml import etree as ET
from datetime import datetime

response_hourly = ''

def get_current_weather(lat, lon, api_key):
    api_call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&mode=xml&lang=fr"
    response = requests.get(api_call)
    if response:
        xml_content = response.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(str(xml_content))

        # Accessing elements
        temperature_value = round(float(root.find('temperature').attrib['value']))
        feels_like_value =round(float(root.find('feels_like').attrib['value']))
        humidity_value = root.find('humidity').attrib['value']
        
        weather_description = root.find('weather').attrib['value']
        wind_speed = round(3.6 * float(root.find('wind/speed').attrib['value']))
        sun_rise_datetime = datetime.strptime(root.find('city/sun').attrib['rise'], '%Y-%m-%dT%H:%M:%S')
        sun_set_datetime = datetime.strptime(root.find('city/sun').attrib['set'], '%Y-%m-%dT%H:%M:%S')
        sun_rise = str(sun_rise_datetime.strftime('%H:%M'))
        sun_set = str(sun_set_datetime.strftime('%H:%M'))

        # clouds_name = root.find('clouds').attrib['name']
        # clouds_value = root.find('clouds').attrib['value']
        # temperature_unit = "°c"#root.find('temperature').attrib['unit']
        # humidity_unit = root.find('humidity').attrib['unit']
        # feels_like_unit = "°c"
        # wind_speed_unit = "km/h"
        # city_name = root.find('city').attrib['name']
        # last_update_value = root.find('lastupdate').attrib['value']
        # wind_speed_name = root.find('wind/speed').attrib['name']
        # wind_direction_value = root.find('wind/direction').attrib['value']
        # wind_direction_code = root.find('wind/direction').attrib['code']
        # wind_direction_name = root.find('wind/direction').attrib['name']
        # pressure_value = root.find('pressure').attrib['value']
        # pressure_unit = root.find('pressure').attrib['unit']
        # visibility_value = root.find('visibility').attrib['value']
        # clouds_unit = "%"


        return {
            "temperature": temperature_value,
            "feels_like_value": feels_like_value,
            "humidity": humidity_value,
            "weather_description": weather_description,
            "wind_speed": wind_speed,
            "sun_rise": sun_rise,
            "sun_set": sun_set
        }

    else:
        raise Exception(f"Non-success status code: {response.status_code}")


def get_hourly_forecast(lat, lon, api_key):
    global response_hourly
    api_call = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}&units=metric&mode=xml&cnt={24}&lang=fr"
    response_hourly = requests.get(api_call)
    
    if response_hourly:
        xml_content = response_hourly.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(xml_content)
        
        # Extract elements
        forecast_times = root.findall('.//forecast/time')
        forecast_data = []

        # Extract data for each hour and store in a list of dictionaries
        for hour in forecast_times:
            date = datetime.strptime(hour.get('from'), '%Y-%m-%dT%H:%M:%S')
            time =  str(date.strftime('%H:%M'))

            wind_speed_mps = float(hour.find('.//windSpeed').get('mps'))
            wind_speed_kph = round(wind_speed_mps * 3.6)

            weather_description = hour.find('.//symbol').get('name')
            precipitation_proba = float(hour.find('.//precipitation').get('probability'))
            temperature = round(float(hour.find('.//temperature').get('value')))
            
            # wind_direction = hour.find('.//windDirection').get('name')
            # feels_like = round(float(hour.find('.//feels_like').get('value')))
            # pressure = float(hour.find('.//pressure').get('value'))
            # humidity = round(float(hour.find('.//humidity').get('value')))            

            data = {
                'time': time,
                'weather_description': weather_description,
                'precipitation_proba': precipitation_proba,
                'wind_speed': wind_speed_kph,
                'temperature': temperature,
            }
            forecast_data.append(data)

        return forecast_data
    else:
        raise Exception(f"Non-success status code: {response_hourly.status_code}")

def get_daily_forecast(lat,lon,api_key):
    api_call = f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={7}&appid={api_key}&mode=xml&units=metric&lang=fr"
    response = requests.get(api_call)
    if response:
        xml_content = response.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(str(xml_content))

        forecast_data = []
        forecast_times = root.findall(".//time")

        for day in forecast_times:
            date = day.get("day")

            temperature_day = round(float(day.find("temperature").get("day")))
            temperature_max = round(float(day.find("temperature").get("max")))
            temperature_min = round(float(day.find("temperature").get("min")))
            wind_speed_mps = float(day.find("windSpeed").get("mps"))
            wind_speed_kmh = round(wind_speed_mps * 3.6)
            weather_description = day.find("symbol").get("name")

            day_data = {
                "date": date,
                "weather_description": weather_description,
                "temperature_day": temperature_day,
                "temperature_max": temperature_max,
                "temperature_min": temperature_min,
                "wind_speed_kmh": wind_speed_kmh
            }
            forecast_data.append(day_data)

        return forecast_data
    else:
        raise Exception(f"Non-success status code: {response.status_code}")


import requests
import xml.etree.ElementTree as ET
from datetime import datetime


def get_model_data():
    global response_hourly

    if response_hourly:
        xml_content = response_hourly.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(xml_content)

        forecast_times = root.findall('.//forecast/time')
        formatted_data = {
            'main': [],
            'description': [],
            'temp': [],
            'feels_like': [],
            'temp_min': [],
            'temp_max': [],
            'pressure': [],
            'humidity': [],
            'visibility': [],
            'speed': [],
            'clouds': []
        }

        for hour in forecast_times:
            weather_description = hour.find('.//symbol').get('name')
            temperature = round(float(hour.find('.//temperature').get('value')))
            feels_like = round(float(hour.find('.//feels_like').get('value')))
            temp_min = None  # This data is not available in the provided function
            temp_max = None  # This data is not available in the provided function
            pressure = float(hour.find('.//pressure').get('value'))
            humidity = round(float(hour.find('.//humidity').get('value'))) 
            visibility = None  # This data is not available in the provided function
            wind_speed_mps = float(hour.find('.//windSpeed').get('mps'))
            wind_speed_kph = round(wind_speed_mps * 3.6)
            clouds = None  # This data is not available in the provided function

            formatted_data['main'].append(weather_description)
            formatted_data['description'].append(weather_description)
            formatted_data['temp'].append(temperature)
            formatted_data['feels_like'].append(feels_like)
            formatted_data['temp_min'].append(temp_min)
            formatted_data['temp_max'].append(temp_max)
            formatted_data['pressure'].append(pressure)
            formatted_data['humidity'].append(humidity)
            formatted_data['visibility'].append(visibility)
            formatted_data['speed'].append(wind_speed_kph)
            formatted_data['clouds'].append(clouds)

        return formatted_data

