from datetime import date
import os, requests, json
from typing import List

from dotenv import load_dotenv


load_dotenv()

def get_stock_info_from_name(stock_name : str) -> tuple : 
    """_summary_ : This function gets the stock information from the stock name.

    Args:
        stock_name (str): The name of the stock.

    Returns:
        _type_: tuple
    """
    stock_name = stock_name.upper()
    url = 'https://ticker-2e1ica8b9.now.sh//keyword/{}'.format(stock_name)
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if len(r.json()) == 0:
        return {}, 404
    return r.json()[0], 200



 
def get_exact_keys_for_stock_info(quote_dict : dict) -> tuple:
    """_summary_ : Get the required keys from the quote dict obtained by api, tailored for personal application

    Args:
        quote_dict (dict): Dict containing info about stock, received from API

    Returns:
        tuple: Returns a tuple with status_code and required data if status_code == 200
    """
    return_dict = {}
    for k,v in quote_dict.items():
        if 'price' in k:
            return_dict['curr_price'] = quote_dict[k]
        elif 'previous close' in k:
            return_dict['prev_close'] = quote_dict[k]
        elif 'latest trading day' in k:
            return_dict['latest_trading_day'] = quote_dict[k]
    if len(return_dict) != 3:
        return {}, 404
    return return_dict, 200

            

def get_stock_info_from_symbol(stock_symbol : str) -> tuple : 
    """_summary_ : This function gets the stock information from the stock symbol.

    Args:
        stock_symbol (str): The symbol of the stock.

    Returns:
        _type_: tuple
    """
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}'.format(stock_symbol,os.environ.get('alpha_vantage_api_key') )
    r = requests.get(url)
    if r.status_code != 200:
        return {}, 404
    if 'Global Quote' in r.json():
        global_quote_dict = r.json()['Global Quote']
        final_tuple = get_exact_keys_for_stock_info(global_quote_dict)
        if final_tuple[1] == 404:
            return {}, 404
        return final_tuple[0], 200
    
def convert_yyyy_mm_dd(date_str : str) -> str:
    """_summary_ : This function converts the date string from yyyy-mm-dd to dd-mm-yyyy

    Args:
        date_str(str): The date string in yyyy-mm-dd format

    Returns:
        _type_: str in dd-mm-yyyy format
    """
    year = date_str.split("-")[0]
    month = date_str.split("-")[1]
    day  = date_str.split("-")[2]
    month = date(int(year), int(month), int(day)).strftime('%B')
    return "{} {} {}".format(day, month, year)

def higher_level_get_stock_details(stock_name : str) -> dict: 
    """_summary_ : This higher level function uses two helpers to first get the symbol from name, and then symbol -> price details

    Args:
        stock_name (str): The name of the stock

    Returns:
        dict: Dict containining info we want to show
    """
    stock_symbol_tuple = get_stock_info_from_name(stock_name=stock_name)
    if stock_symbol_tuple[1] == 404:
        return {}
    stock_symbol_dict = stock_symbol_tuple[0]
    if 'symbol' in stock_symbol_dict:
        symbol_name = stock_symbol_dict['symbol']
        stock_final_tuple = get_stock_info_from_symbol(symbol_name)
        if stock_final_tuple[1] == 404:
            return {}
        stock_final_dict = stock_final_tuple[0]
        if 'latest_trading_day' in stock_final_dict:
            stock_final_dict['latest_trading_day'] = convert_yyyy_mm_dd(stock_final_dict['latest_trading_day'])
        return stock_final_dict
    else:
        return {}

    

   

