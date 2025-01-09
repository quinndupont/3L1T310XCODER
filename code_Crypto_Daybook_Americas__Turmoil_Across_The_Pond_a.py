

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Create a function to gather data from Coindesk
def get_coindesk_data():
    # Specify the URL for Coindesk API
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    # Send a GET request and store the response as a JSON object
    response = requests.get(url).json()
    
    # Extract relevant data from the JSON object
    # Current price of Bitcoin in USD
    btc_price = response['bpi']['USD']['rate_float']
    
    # Timestamp when the data was retrieved
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create a dictionary to store the data
    data = {'Timestamp': timestamp, 'BTC Price (USD)': btc_price}
    
    return data

# Create a function to gather news data from a specified source
def get_news_data(source):
    # Specify the URL for the news source
    url = "https://newsapi.org/v2/top-headlines?sources=" + source + "&apiKey=API_KEY"
    
    # Send a