
import random, json

def return_random_movie() -> dict:
    """_summary_ : This function returns a random movie from the list of movies.

    Returns:
        dict: The movie details.
    """
    with open('./api/movies.json') as f:
        movies = json.load(f)
    return random.choice(movies)

