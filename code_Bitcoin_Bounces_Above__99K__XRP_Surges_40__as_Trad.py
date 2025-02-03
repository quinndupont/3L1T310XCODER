

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Define function to retrieve latest price data for Bitcoin and XRP from Coindesk
def get_crypto_data():
    # Retrieve data from Coindesk API
    btc_url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    xrp_url = "https://api.coindesk.com/v1/bpi/currentprice/XRP.json"
    btc_data = pd.read_json(btc_url)
    xrp_data = pd.read_json(xrp_url)

    # Store data in pandas dataframe
    btc_df = btc_data['bpi'].to_frame()
    xrp_df = xrp_data['bpi'].to_frame()

    # Rename columns to 'BTC' and 'XRP'
    btc_df.columns = ['BTC']
    xrp_df.columns = ['XRP']

    # Convert date column to datetime format
    btc_df.index = pd.to_datetime(btc_df.index)
    xrp_df.index = pd.to_datetime(xrp_df.index)

    return btc_df, xrp_df

# Call function to retrieve data
btc_df, xrp_df = get_crypto