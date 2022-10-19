from numpy import cov
import requests
import json

from dotenv import load_dotenv
import os

load_dotenv()

from api.weather_api import higher_level_weather_return
from api.news_api import get_news
from api.random_movie import return_random_movie
from api.stocks import higher_level_get_stock_details
from api.covid_api import get_covid_stats

def format_cmd_msg(name : str) -> str: 
    """_summary_ : This function formats the message that contains all the commands that the user can use to interact with the bot.

    Args:
        name (str): The name of the user.

    Returns:
        str: The formatted message, containing all commands.
    """
    cmd = 'Hi ' + name + '! Here are the commands you can use: \n'
    cmd = cmd + '\u2022 help - Get a list of commands \n'
    cmd = cmd + '\u2022 price <stock_name> - Get latest prices of your favourite assets \n'
    cmd = cmd + '\u2022 weather <city_name> - Get weather report \n'
    cmd = cmd + '\u2022 news - Get latest news \n'
    cmd = cmd + '\u2022 movie - Get a movie recommendation \n'
    cmd = cmd + '\u2022 joke - Read a joke \n'
    cmd = cmd + '\u2022 google <search_query> - Search on Google \n'
    cmd = cmd + '\u2022 wiki <search_query> - Search on Wikipedia \n'
    cmd = cmd + '\u2022 youtube <search_query> - Search on YouTube \n'
    cmd = cmd + '\u2022 covid - Get latest covid stats \n'
    return cmd

def format_stocks_message(stock_name : str) -> str: 
    """_summary_ : This function formats the stock info message to be sent to the user

    Args:
        stock_name (str): The name of the stock

    Returns:
        str: The formatted stock message
    """
    stock_dict = higher_level_get_stock_details(stock_name)
    if stock_dict == {}:
        return 'Stock not found. Please try again.'
    stock_str = 'Here is the latest info for ' + stock_name.title() + ':\n'
    stock_str = stock_str + '\u2022Current price: ' + str(stock_dict['curr_price']) + '\n'
    stock_str = stock_str + '\u2022Previous Close: ' + str(stock_dict['prev_close']) + '\n'
    stock_str = stock_str + '\u2022Latest Trading Date: ' + str(stock_dict['latest_trading_day']) + '\n'
    return stock_str

def format_covid_message(country_name : str) -> str:
    """_summary_ : This function formats the covid message to be sent to the user.

    Args:
        country_name (str): The name of the country.

    Returns:
        str: The formatted covid message.
    """
    covid_str = ''
    covid_dict = {}
    if country_name == '':
        covid_tuple = get_covid_stats(country_name)
        if covid_tuple[1] == 404:
            return 'Data not found. Please try again.'
        covid_dict = covid_tuple[0]
        covid_str = 'Here are the latest covid stats worldwide: \n'
    else:
        covid_tuple = get_covid_stats(country_name)
        if covid_tuple[1] == 404:
            return 'Data not found for {}. Please try again.'.format(country_name)
        covid_dict = covid_tuple[0]
        covid_str = 'Here are the latest covid stats for {}: \n'.format(country_name.title())
    covid_str = covid_str + '\u2022Total cases: ' + str(covid_dict['confirmed']) + '\n'
    covid_str = covid_str + '\u2022Total deaths: ' + str(covid_dict['deaths']) + '\n'
    return covid_str
        
        
def format_news_message() -> str:
    """_summary_ : This function formats the news message to be sent to the user.

    Returns:
        str: The formatted news message.
    """
    news_tuple = get_news()
    if news_tuple[1] == 404:
        return 'No news found. Please try again.'
    news_dict = news_tuple[0]
    news_str = 'Here are the latest news: \n'
    for k,v in news_dict.items():
        #Show key : value, key is headline and value is url
        news_str = news_str + '\u2022' + k + ' : ' + v + '\n'
    return news_str

def format_weather_message(city_name : str) -> str:
    """_summary_ : This is a higher-level function, which formats the weather report, to be sent to the user.

    Args:
        city_name (str): The name of the city.

    Returns:
        _type_: str
    """
    weather_tuple = higher_level_weather_return(city_name.lower())
    if weather_tuple[1] == 404:
        return 'City not found. Please try again.'
    weather_dict = weather_tuple[0]
    weather_str = 'Weather report for ' + weather_dict['city_name'] + ':\n'
    weather_str = weather_str + '\u2022Curent temperature: ' + str(weather_dict['current_temp']) + '°C\n'
    weather_str = weather_str + '\u2022Feels like: ' + str(weather_dict['feels_like']) + '°C\n'
    weather_str = weather_str + "\u2022Today's high: " + str(weather_dict['max_temp']) + '°C\n'
    weather_str = weather_str + "\u2022Today's low: " + str(weather_dict['min_temp']) + '°C\n'
    weather_str = weather_str + '\u2022Wind speed: ' + str(weather_dict['wind_speed']) + ' km/h\n'
    return weather_str

def format_movie_message() -> str:
    """_summary_ : This function formats the movie message to be sent to the user.
    Args : None
    Returns:
        str: The formatted movie message.
    """
    random_movie_dict = return_random_movie()
    movie_str = 'Here is a movie recommendation for you: \n'
    movie_str =  movie_str + '\u2022Title: ' + random_movie_dict['title'] + ' (' + random_movie_dict['year'] + ') \n'
    genre_arr = random_movie_dict['genres']
    if len(genre_arr) == 1:
        movie_str = movie_str + '\u2022Genre: ' + genre_arr[0] 
    else:
        genre_str = ''
        for g in genre_arr:
            g = g.strip()
            genre_str = genre_str + g + ', '
        genre_str = genre_str[:-2]
        movie_str = movie_str + '\u2022Genres: ' + genre_str 
    return movie_str



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