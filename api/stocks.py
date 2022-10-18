import os, requests, json

def convert_name_to_ticker(stock_name : str) -> str:
    url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&callback=YAHOO.Finance.SymbolSuggest.ssCallback'.format(stock_name)
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    print(r.json())

convert_name_to_ticker('apple')