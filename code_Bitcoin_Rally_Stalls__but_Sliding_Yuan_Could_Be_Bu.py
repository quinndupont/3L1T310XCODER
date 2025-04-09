

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Define function to retrieve real-time data from Coindesk
def get_coindesk_data():
    # Make API call to Coindesk for current Bitcoin price in USD
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # Convert response to JSON format
    data = response.json()
    # Retrieve current Bitcoin price in USD
    bitcoin_price = data['bpi']['USD']['rate_float']
    
    # Make API call to Coindesk for historical Bitcoin price data
    response = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-01-01&end=2021-08-31")
    # Convert response to JSON format
    data = response.json()
    # Store data in a Pandas dataframe
    df_bitcoin = pd.DataFrame.from_dict(data['bpi'], orient='index', columns=['price'])
    # Convert index to datetime format
    df_bitcoin.index = pd.to_datetime(df_bitcoin.index)
    
    # Make API call to Coindesk for current Chinese