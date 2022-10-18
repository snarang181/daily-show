import requests
import json

from api.shorten_url import shorten_url

def get_news_api() -> tuple:
    """_summary_ : This function gets the news from the news API.
    Args: None
    Returns:
        _type_: tuple
    """
    url = "https://bing-news-search1.p.rapidapi.com/news/trendingtopics"

    querystring = {"textFormat":"Raw","safeSearch":"Off", "mkt" : "en-US", "sortBy" : "Date"}

    headers = {
        "X-BingApis-SDK": "true",
        "X-RapidAPI-Key": "02b83b8ac7msh6d534121113bb86p13b8d9jsn0f8a71b13b13",
        "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_arr = response.json()['value'] if response.status_code == 200 else []
    if response_arr == []:
        return [], 404
    return (response_arr[:3] if len(response_arr) > 3 else response_arr), 200

def get_news() -> tuple:
    """_summary_ : This function formats the news.
    Args : None
    Returns:
        tuple: _description_
    """
    news_tuple = get_news_api()
    if news_tuple[1] == 404:
        return {}, 404
    news_dict = {}
    for news in news_tuple[0]:
        news_dict[news['query']['text']] = news['newsSearchUrl']
    return news_dict, 200


        