import requests
from lxml import etree as ET
import datetime


def get_current_weather(lat, lon, api_key):
    api_call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&mode=xml&lang=fr"
    response = requests.get(api_call)
    if response:
        xml_content = response.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(str(xml_content))

        timezone = datetime.timedelta(seconds=float(root.find('.//timezone').text))

        # Accessing elements
        temperature_value = round(float(root.find('temperature').attrib['value']))
        feels_like_value =round(float(root.find('feels_like').attrib['value']))
        humidity_value = root.find('humidity').attrib['value']
        
        weather_description = root.find('weather').attrib['value']
        wind_speed = round(3.6 * float(root.find('wind/speed').attrib['value']))
        weather_code = root.find('weather').attrib['number']
        weather_icon = root.find('weather').attrib['icon']
        sun_rise_datetime = datetime.datetime.strptime(root.find('city/sun').attrib['rise'], '%Y-%m-%dT%H:%M:%S') + timezone
        sun_set_datetime = datetime.datetime.strptime(root.find('city/sun').attrib['set'], '%Y-%m-%dT%H:%M:%S') + timezone
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

        print("get_current_weather passed")
        return {
            "temperature": temperature_value,
            "feels_like_value": feels_like_value,
            "code": weather_code,
            "weather_icon":  weather_icon,
            "humidity": humidity_value,
            "weather_description": weather_description,
            "wind_speed": wind_speed,
            "sun_rise": sun_rise,
            "sun_set": sun_set
        }

    else:
        raise Exception(f"Non-success status code: {response.status_code}")

def get_hourly_forecast(lat, lon, api_key):
    api_call = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}&units=metric&mode=xml&cnt={32}&lang=fr"
    response = requests.get(api_call)
    if response:
        xml_content = response.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(xml_content)
        
        # Extract elements
        forecast_times = root.findall('.//forecast/time')
        forecast_data = []
        timezone = datetime.timedelta(seconds=float(root.find('.//timezone').text))
        
        # Extract data for each hour and store in a list of dictionaries
        count = 0
        for hours in forecast_times:
            date = datetime.datetime.strptime(hours.get('from'), '%Y-%m-%dT%H:%M:%S')
            time =  str(date.strftime('%H H'))

            wind_speed_mps = float(hours.find('.//windSpeed').get('mps'))
            wind_speed_kph = round(wind_speed_mps * 3.6)

            weather_code = hours.find('.//symbol').get('var')
            weather_icon = hours.find('.//symbol').get('number')
            weather_description = hours.find('.//symbol').get('name')
            precipitation_proba = round(float(hours.find('.//precipitation').get('probability'))*100)
            temperature = round(float(hours.find('.//temperature').get('value')))
            
            # wind_direction = hour.find('.//windDirection').get('name')
            # feels_like = round(float(hour.find('.//feels_like').get('value')))
            # pressure = float(hour.find('.//pressure').get('value'))
            # humidity = round(float(hour.find('.//humidity').get('value')))
            
            if date >= (datetime.datetime.now(datetime.UTC).replace(tzinfo=None) + timezone):
                if count >= 24:
                    print("get_hourly_forecast passed")
                    count = 0
                    return forecast_data
                
                data = {
                    'time': time,
                    "code": weather_code,
                    "weather_icon": weather_icon,
                    'weather_description': weather_description,
                    'precipitation_proba': precipitation_proba,
                    'wind_speed': wind_speed_kph,
                    'temperature': temperature,
                }
                forecast_data.append(data)
                count += 1
        print("get_hourly_forecast passed")
        count = 0
        return forecast_data
    else:
        raise Exception(f"Non-success status code: {response.status_code}")

def get_daily_forecast(lat, lon, api_key):
    api_call = f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&appid={api_key}&mode=xml&units=metric&lang=fr&cnt={8}"
    response = requests.get(api_call)
    if response:
        xml_content = response.text.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        root = ET.fromstring(str(xml_content))

        forecast_data = []
        forecast_times = root.findall(".//time")[1:]

        for day in forecast_times:
            
            date = day.get("day")
            weather_code = day.find('.//symbol').get('var')
            weather_icon = day.find('.//symbol').get('number')

            temperature_day = round(float(day.find("temperature").get("day")))
            temperature_max = round(float(day.find("temperature").get("max")))
            temperature_min = round(float(day.find("temperature").get("min")))
            wind_speed_mps = float(day.find("windSpeed").get("mps"))
            wind_speed_kmh = round(wind_speed_mps * 3.6)
            weather_description = day.find("symbol").get("name")
            
            
            day_data = {
                "date": date,
                "code": weather_code,
                "weather_icon": weather_icon,
                "weather_description": weather_description,
                "temperature_day": temperature_day,
                "temperature_max": temperature_max,
                "temperature_min": temperature_min,
                "wind_speed_kmh": wind_speed_kmh
            }
            forecast_data.append(day_data)
        
        print("get_daily_forecast passed")
        return forecast_data
    else:
        raise Exception(f"Non-success status code: {response.status_code}")

# ICI FAIRE LA MODIFICATION POUR LE DATAMODELE AUSSI
def weather_data_model(lat, lon, api_key):
    api_call = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}&units=metric&cnt={24}"
    response = requests.get(api_call)
    
    if response.status_code != 200:
        print("Erreur lors de la récupération des données météorologiques.")
        return None
    
    data = response.json()
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
    
    for item in data['list']:
        formatted_data['main'].append(item['weather'][0]['main'])
        formatted_data['description'].append(item['weather'][0]['description'])
        formatted_data['temp'].append(item['main']['temp'])
        formatted_data['feels_like'].append(item['main']['feels_like'])
        formatted_data['temp_min'].append(item['main']['temp_min'])
        formatted_data['temp_max'].append(item['main']['temp_max'])
        formatted_data['pressure'].append(item['main']['pressure'])
        formatted_data['humidity'].append(item['main']['humidity'])
        formatted_data['visibility'].append(item['visibility'])
        formatted_data['speed'].append(item['wind']['speed'])
        formatted_data['clouds'].append(item['clouds']['all'])
    print("weather_data_model passed")
    return formatted_data