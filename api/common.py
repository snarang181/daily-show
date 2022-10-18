import requests
import json

from dotenv import load_dotenv
import os

load_dotenv()

from api.weather_api import higher_level_weather_return


def format_cmd_msg(name : str) -> str: 
    """_summary_ : This function formats the message that contains all the commands that the user can use to interact with the bot.

    Args:
        name (str): The name of the user.

    Returns:
        str: The formatted message, containing all commands.
    """
    cmd = 'Hi ' + name + '! Here are the commands you can use: \n'
    cmd = cmd + '\u2022 help - Get a list of commands \n'
    cmd = cmd + '\u2022 joke - Read a joke \n'
    cmd = cmd + '\u2022 price - Get latest prices \n'
    cmd = cmd + '\u2022 weather <city_name> - Get weather report \n'
    return cmd

def format_weather_message(city_name : str) -> str:
    """_summary_ : This is a higher-level function, which formats the weather report, to be sent to the user.

    Args:
        city_name (str): The name of the city.

    Returns:
        _type_: str
    """
    weather_tuple = higher_level_weather_return(city_name.lower())
    if weather_tuple[1] == 404:
        return 'City not found'
    weather_dict = weather_tuple[0]
    weather_str = 'Weather report for ' + weather_dict['city_name'] + ':\n'
    weather_str = weather_str + '\u2022Curent temperature: ' + str(weather_dict['current_temp']) + '°C\n'
    weather_str = weather_str + '\u2022Feels like: ' + str(weather_dict['feels_like']) + '°C\n'
    weather_str = weather_str + "\u2022Today's high: " + str(weather_dict['max_temp']) + '°C\n'
    weather_str = weather_str + "\u2022Today's low: " + str(weather_dict['min_temp']) + '°C\n'
    weather_str = weather_str + '\u2022Wind speed: ' + str(weather_dict['wind_speed']) + ' km/h\n'
    return weather_str


def send_message_meta_api_call(phone_num : str , phone_num_id : str , message : str, name : str) -> None:
    """_summary_ : This function sends a message to the user using the Meta API.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        message (str): The message to be sent to the user.
        name (str): The name of the user.

    Returns:
        _type_: None
    """
    meta_auth_token = 'Bearer ' + os.environ.get('meta_api_token')   
    base_url = 'https://graph.facebook.com/v13.0/' + str(phone_num_id) + '/messages'
    headers = {'Authorization' : meta_auth_token, 'Content-Type': 'application/json'}
    body = {
        "messaging_product" : "whatsapp", "recipient_type" : "individual", "to" : str(phone_num) , "type" : "text" , "text" : {
            "preview_url" : False,
            "body" : str(message)
        }
    }
    r = requests.post(base_url, data=json.dumps(body), headers=headers)
    return None