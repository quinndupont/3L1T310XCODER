

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime

# Create a list of cryptocurrencies to analyze
crypto_list = ['Dogecoin', 'XRP', 'Bitcoin']

# Function to gather real-time data from CoinMarketCap
def get_data(crypto):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}/'.format(crypto)
    response = requests.get(url)
    data = response.json()
    return data[0]

# Function to convert timestamp to date
def convert_date(timestamp):
    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    return date

# Function to plot historical performance of a cryptocurrency
def plot_performance(data, crypto):
    # Create a dataframe with the necessary columns
    df = pd.DataFrame(data, columns=['date', 'price_usd', 'volume_usd', 'market_cap_usd'])
    # Convert the timestamp to date
    df['date'] = df['date'].apply(convert_date)
    # Convert the price, volume, and market cap to numeric values
    df['price_usd'] = pd.to_numeric(df['price_usd'])
    df['