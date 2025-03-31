

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Define function to gather data from various sources
def gather_data():
    
    # Use requests library to get data from CryptoCompare API
    url = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=365"
    response = requests.get(url)
    data = response.json()['Data']
    
    # Convert data into a pandas dataframe
    df = pd.DataFrame(data)
    
    # Drop unnecessary columns
    df.drop(['volumeto', 'conversionType', 'conversionSymbol'], axis=1, inplace=True)
    
    # Convert timestamp to readable date format
    df['time'] = pd.to_datetime(df['time'], unit='s')
    
    # Return dataframe
    return df

# Define function to plot Bitcoin price movement
def plot_price_movement(df):
    
    # Plot Bitcoin price over time
    plt.figure(figsize=(12,6))
    plt.plot(df['time'], df['close'], color='blue')
    plt.xlabel('Date')
    plt.ylabel('Bitcoin Price (USD)')
    plt.title('Bitcoin Price Movement')
   