import requests
import json
from dotenv import load_dotenv
import os
from api.joke_generate import get_rand_joke
from api.common import format_cmd_msg, send_message_meta_api_call, format_weather_message, format_news_message, format_movie_message, format_stocks_message, format_covid_message



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

def send_stocks_message(phone_num : str, phone_num_id : str, name : str, stock_name : str) -> None:
    """_summary_ : This is a higher-level function, which sends a stock info message to the user

    Args:
        phone_num (str): THe phone number of the user
        phone_num_id (str): The phone number ID of the user
        name (str): The name of the user
        stock_name (str): The name of the stock
    """
    stock_message = format_stocks_message(stock_name)
    send_message_meta_api_call(phone_num, phone_num_id, stock_message, name)
    
def send_covid_message(phone_num : str, phone_num_id : str, name : str, country_name : str) -> None:
    """_summary_ : This is a higher-level function, which sends a covid message to the user.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        name (str): The name of the user.

    Returns:
        _type_: None
    """
    covid_message = format_covid_message(country_name)
    send_message_meta_api_call(phone_num, phone_num_id, covid_message, name)
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

def send_movie_message(phone_num : str, phone_num_id : str, name : str) -> None:
    """_summary_ : This is a higher-level function, which sends a movie message to the user.

    Args:
        phone_num (str): The phone number of the user.
        phone_num_id (str): The phone number ID of the user.
        name (str): The name of the user.

    Returns:
        _type_: None
    """
    movie_message = format_movie_message()
    send_message_meta_api_call(phone_num, phone_num_id, movie_message, name)
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



    
    
    