

# Import necessary libraries
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# Define function to retrieve historical price data from CoinMarketCap
def get_historical_data(coin, start_date, end_date):
    # Define URL and parameters for API call
    base_url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical'
    params = {'slug': coin, 'convertId': '2781', 'timeStart': start_date, 'timeEnd': end_date}
    
    # Make API call and store response as JSON
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Extract data from JSON and store as dataframe
    prices = data['data']['quotes']
    df = pd.DataFrame(prices)
    
    # Convert timestamp to datetime format and set as index
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')
    
    # Convert prices to numeric type
    df['price'] = pd.to_numeric(df['price'])
    
    # Return dataframe
    return df

# Define function to calculate percentage change in price
def calculate