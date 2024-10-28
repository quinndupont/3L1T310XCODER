

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json

# Define function to get historical data for Tether and overall crypto market
def get_historical_data():
    # Set start and end date for data
    start = "2020-01-01"
    end = "2021-01-01"

    # Get data for Tether and overall crypto market from CoinMarketCap API
    tether_data = requests.get('https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=825&convertId=2781&timeStart='+start+'&timeEnd='+end).json()
    crypto_data = requests.get('https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart='+start+'&timeEnd='+end).json()

    # Convert data to pandas dataframe
    tether_df = pd.DataFrame(tether_data['data']['quotes'])
    crypto_df = pd.DataFrame(crypto_data['data']['quotes'])

    # Rename columns
    tether_df = tether_df[['time_open', 'price_close']]
    tether_df.columns = ['date', 'tether_price']
