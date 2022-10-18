import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def convert_city_to_lat_long(city_name : str) -> dict:
    """_summary_ : This function converts the city name to latitude and longitude.

    Args:
        city_name (str): The name of the city.

    Returns:
        dict: The latitude and longitude of the city.
    """
    weather_api_key = os.environ.get('weather_api_key') 
    url = 'http://api.openweathermap.org/geo/1.0/direct?q={}&appid={}'.format(city_name,weather_api_key)
    r  = requests.get(url, headers = {'Content-Type': 'application/json'})
    api_incoming_data = r.json()
    if len(api_incoming_data) == 0:
        return {"lat" : 0, "lon" : 0}, 404
    return {'lat' : api_incoming_data[0]['lat'], 'lon' : api_incoming_data[0]['lon'],'city_name' : api_incoming_data[0]['name']}, 200

def get_weather_data(lat : float, lon : float) -> dict:
    """_summary_ : This function gets the weather data of a city.

    Args:
        lat (float): The latitude of the city.
        lon (float): The longitude of the city.

    Returns:
        dict: The weather data of the city.
    """
    weather_api_key = os.environ.get('weather_api_key') 
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units={}'.format(lat,lon,weather_api_key,'metric')
    r = requests.get(url, headers = {'Content-Type': 'application/json'})
    weather_data = r.json()
    
    return {'current_temp' : round(float(weather_data['main']['temp'])), 'feels_like' : round(float(weather_data['main']['feels_like'])), 'min_temp' : round(float(weather_data['main']['temp_min'])), 'max_temp' : round(float(weather_data['main']['temp_max'])), 'humidity' : weather_data['main']['humidity'], 'wind_speed' : round(float(weather_data['wind']['speed']) * 3.6),'weather_desc' : weather_data['weather'][0]['description']}

def higher_level_weather_return(city_name : str) -> dict:
    """_summary_ : This function returns the weather data of a city.

    Args:
        city_name (str): The name of the city.

    Returns:
        dict: The weather data of the city.
    """
    lat_long_tuple = convert_city_to_lat_long(city_name)
    if lat_long_tuple[1] == 404:
        return {'current_temp' : 0, 'feels_like' : 0, 'min_temp' : 0, 'max_temp' : 0, 'humidity' : 0, 'wind_speed' : 0,'weather_desc' : 'City not found'}, 404
    lat_long = lat_long_tuple[0]
    weather_data = get_weather_data(lat_long['lat'], lat_long['lon'])
    weather_data['city_name'] = lat_long['city_name']
    return weather_data, 200




   


