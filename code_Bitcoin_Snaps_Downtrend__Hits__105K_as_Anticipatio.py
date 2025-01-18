

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# Function to retrieve historical Bitcoin price data from CoinDesk API
def get_bitcoin_price_data():
    # Specify API URL
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-01-01&end=2017-01-31'
    # Send GET request and store response
    response = requests.get(url)
    # Convert response to JSON format
    bitcoin_price_data = response.json()
    # Extract Bitcoin price data from JSON format
    bitcoin_price_data = bitcoin_price_data['bpi']
    # Create a DataFrame from Bitcoin price data
    bitcoin_price_df = pd.DataFrame.from_dict(bitcoin_price_data, orient='index', columns=['Price (USD)'])
    return bitcoin_price_df

# Function to retrieve news articles related to Trump's stance on Bitcoin using Google News API
def get_trump_bitcoin_news():
    # Specify API URL
    url = 'https://newsapi.org/v2/everything?q=trump+bitcoin&from=2017-01-01&to=2017