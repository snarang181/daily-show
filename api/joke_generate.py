import requests
import json
from dotenv import load_dotenv
import os


def get_rand_joke() -> str:
    """_summary_ : This function gets a random joke from the joke API.
    Args: None
    Returns:
        _type_: str
    """
    r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    return r.json()['joke']

