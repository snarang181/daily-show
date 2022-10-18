import requests
import json
from dotenv import load_dotenv
import os
from api.joke_generate import get_rand_joke
from api.common import format_cmd_msg, send_message_meta_api_call, format_weather_message, format_news_message



load_dotenv()

def send_all_commands_message(phone_num : str , phone_num_id : str, name : str) -> None:
    """_summary_ : This is a higher-level function, which sends a message to the user containing all the commands that the user can use to interact with the bot.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        name (str): The name of the user.

    Returns:
        _type_: None
    """
    msg = format_cmd_msg(name)
    send_message_meta_api_call(phone_num, phone_num_id, msg, name)
    return None

def send_news_message(phone_num : str , phone_num_id : str, name : str) -> None:
    """_summary_ : This is a higher-level function, which sends a news message to the user.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        name (str): The name of the user.

    Returns:
        _type_: None
    """
    news_message = format_news_message()
    send_message_meta_api_call(phone_num, phone_num_id, news_message, name)
    return None

def send_weather_message(phone_num : str, phone_num_id : str,  name : str, city_name : str,) -> None:
    """_summary_ : This is a higher-level function, which sends a weather report to the user.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        name (str): The name of the user.
        city_name (str): The name of the city.

    Returns:
        _type_: None
    """
    weather_message = format_weather_message(city_name)
    send_message_meta_api_call(phone_num, phone_num_id, weather_message, name)
    return None


def send_joke(phone_num : str, phone_num_id : str, name : str) -> None:
    """_summary_ : This is a higher-level function, which sends a joke to the user.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        name (str): The name of the user.

    Returns:
        _type_: None
    """
    joke = get_rand_joke()
    send_message_meta_api_call(phone_num, phone_num_id, joke, name)
    return None



    
    
    