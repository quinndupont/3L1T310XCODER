

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Define function to get real-time data from CoinMarketCap
def get_data(symbol):
    """
    Function to get real-time data from CoinMarketCap for a given cryptocurrency symbol.
    :param symbol: cryptocurrency symbol, ex: ADA, BTC
    :return: pandas DataFrame with price, volume, and market cap data
    """
    # Construct API URL
    url = f'https://api.coinmarketcap.com/v1/ticker/{symbol}/?convert=USD'
    # Get response from API
    response = requests.get(url)
    # Convert response to JSON format
    data = response.json()
    # Create DataFrame from JSON data
    df = pd.DataFrame(data)
    # Keep only relevant columns
    df = df[['symbol', 'price_usd', '24h_volume_usd', 'market_cap_usd', 'last_updated']]
    # Convert last_updated column to datetime format
    df['last_updated'] = pd.to_datetime(df['last_updated'], unit='s')
    # Set index as last_updated column
    df.set_index('last_updated', inplace=True)
    # Convert data types