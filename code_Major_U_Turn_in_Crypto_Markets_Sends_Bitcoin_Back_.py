

# Import necessary libraries
import requests
import json
import pandas as pd
from textblob import TextBlob

# Define function to retrieve current price of Bitcoin
def get_current_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        btc_price = data["bpi"]["USD"]["rate_float"]
        return btc_price
    else:
        print("Error retrieving current price of Bitcoin.")
        return None

# Define function to retrieve historical price data of Bitcoin
def get_historical_btc_data():
    url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-05-01&end=2021-05-31"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        btc_data = data["bpi"]
        return btc_data
    else:
        print("Error retrieving historical price data of Bitcoin.")
        return None

# Define function to retrieve news articles and social media posts related to the U-turn
def get_related_posts():
    # Retrieve news articles