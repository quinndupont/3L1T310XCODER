

# Import necessary libraries
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob

# Function to gather real-time data on Bitcoin's price from multiple exchanges
def get_bitcoin_price():
    # List of exchanges to gather data from
    exchanges = ['Coinbase', 'Binance', 'Kraken', 'Gemini']
    # Dictionary to store data
    bitcoin_data = {}
    # Loop through each exchange
    for exchange in exchanges:
        # Make API call to get Bitcoin's price
        response = requests.get('https://api.cryptowat.ch/markets/bitfinex/btcusd/price')
        # Convert response to JSON format
        json_response = response.json()
        # Get latest price
        price = json_response['result']['price']
        # Add price to dictionary with exchange name as key
        bitcoin_data[exchange] = price
    # Convert dictionary to dataframe
    df = pd.DataFrame.from_dict(bitcoin_data, orient='index', columns=['Price (USD)'])
    # Plot a line chart to visualize trend over the past few weeks
    df.plot(kind='line', xlabel='Date', ylabel='Price (USD