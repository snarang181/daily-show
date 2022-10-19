import os, requests, json


def get_country_id_from_name(country_name : str) -> str:
    """_summary_ : This function returns the country id from the country name.

    Args:
        country_name (str): The name of the country.

    Returns:
        str: The country id.
    """
    with open('./api/dataset/covid_data.json') as f:
        countries = json.load(f)
        if country_name in countries:
            return (countries[country_name], 200)
        else:
            return ('Country not found', 404)


def get_covid_stats(country_name : str) -> tuple:
    """_summary_ : This function returns the covid stats of the country.

    Args:
        country_name (str): The name of the country.

    Returns:
        tuple: The covid stats of the country and the status code.
    """
    covid_dict = {}
    if country_name == '':
        url = 'http://coronavirus-tracker-api.herokuapp.com/v2/locations/'
        r = requests.get(url, headers={'Content-Type': 'application/json'})
        if r.status_code == 200:
            covid_dict['confirmed'] = r.json()['latest']['confirmed']
            covid_dict['deaths'] = r.json()['latest']['deaths']
            return (covid_dict, 200)
        else:
            return ({} , 404)
    else:
        country_tuple = get_country_id_from_name(country_name.upper())
        if country_tuple[1] == 404:
            return {}, 404
        country_id = country_tuple[0]
        url = 'http://coronavirus-tracker-api.herokuapp.com/v2/locations/{}'.format(country_id)
        r = requests.get(url, headers={'Content-Type': 'application/json'})
        if r.status_code == 200:
            latest = r.json()['location']['latest']
            if 'confirmed' in latest:
                covid_dict['confirmed'] = latest['confirmed']
            if 'deaths' in latest:
                covid_dict['deaths'] = latest['deaths']
            return (covid_dict, 200)
        else:
            return ({} , 404)
    
