import requests
import json
from dotenv import load_dotenv
import os


def get_rand_joke():
    r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    return r.json()['joke']

