

# Import necessary libraries
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Function to collect real-time data on the Bitcoin market
def collect_data():
    # Use requests library to get data from API
    response = requests.get('https://api.coincap.io/v2/assets/bitcoin/history?interval=d1')
    # Convert response to JSON format
    data = json.loads(response.text)
    # Create a dataframe to store the data
    df = pd.DataFrame(data['data'])
    # Convert timestamp to datetime format and set it as index
    df['date'] = pd.to_datetime(df['date'], unit='ms')
    df.set_index('date', inplace=True)
    return df

# Function to identify dip-buyers
def identify_dip_buyers(df):
    # Calculate 7-day rolling average of price
    df['rolling_avg'] = df['priceUsd'].rolling(window=7).mean()
    # Identify dips as price below rolling average
    df['dip'] = np.where(df['priceUsd'] < df['rolling_avg'], 1, 0)
    # Calculate frequency of dips
    dip_frequency