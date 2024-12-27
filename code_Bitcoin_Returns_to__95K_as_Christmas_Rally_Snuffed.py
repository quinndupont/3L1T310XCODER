

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from textblob import TextBlob

# Define function to collect data from cryptocurrency exchanges
def get_data(exchange, currency):
    """
    Function to collect data from a specific cryptocurrency exchange and currency pair
    :param exchange: name of the cryptocurrency exchange
    :param currency: currency pair (e.g. BTC-USD)
    :return: dataframe with date, price, volume, and market cap
    """
    # Create URL to request data from the exchange
    url = "https://api.coingecko.com/api/v3/exchanges/{}/tickers?base_pair={}".format(exchange, currency)

    # Make GET request and store response in variable
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Convert response to json format
        data = response.json()

        # Create empty lists to store data
        date = []
        price = []
        volume = []
        market_cap = []

        # Loop through each ticker and extract necessary data
        for ticker in data['tickers']:
            date.append(ticker['last