

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Define function to retrieve historical price data from CoinGecko API
def get_price_data(crypto, currency, start_date, end_date):
    """
    Retrieves historical price data for a cryptocurrency in a specific currency from CoinGecko API.
    
    Args:
        crypto (str): Cryptocurrency symbol (e.g. "XRP")
        currency (str): Currency symbol (e.g. "USD")
        start_date (str): Start date in format "dd-mm-yyyy"
        end_date (str): End date in format "dd-mm-yyyy"
        
    Returns:
        df (pandas.DataFrame): Dataframe containing price data
    """
    # Construct API URL
    base_url = 'https://api.coingecko.com/api/v3/coins/{crypto}/market_chart/range?vs_currency={currency}&from={start_date}&to={end_date}'
    url = base_url.format(crypto=crypto, currency=currency, start_date=start_date, end_date=end_date)
    
    # Make API request and retrieve data
    response = requests.get(url)
    data = response.json()
    
    # Convert data