

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
from datetime import datetime, timedelta

# Function to retrieve real-time data on Bitcoin and XRP prices
def get_crypto_prices():
    # Set up API endpoint and parameters
    url = "https://api.coinbase.com/v2/prices/"
    params = {"currency_pair": "BTC-USD, XRP-USD"}
    
    # Make API request and store response in a variable
    response = requests.get(url, params=params)
    
    # Convert response to JSON format
    data = response.json()
    
    # Extract current prices for Bitcoin and XRP
    btc_price = data['data'][0]['amount']
    xrp_price = data['data'][1]['amount']
    
    # Return prices as a dictionary
    return {"BTC": float(btc_price), "XRP": float(xrp_price)}

# Set up variables for data collection
start_date = datetime.today()
end_date = start_date + timedelta(days=7)
hours = pd.date_range(start=start_date, end=end_date, freq='H')

# Create empty lists to store data
btc_prices =