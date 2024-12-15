

# Import necessary libraries
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from textblob import TextBlob
%matplotlib inline

# Define function to pull real-time data from Nasdaq website
def get_nasdaq_data(symbol):
    # Construct API url
    url = 'https://api.nasdaq.com/api/quote/{}/info?assetclass=stocks'.format(symbol)
    # Make request
    response = requests.get(url)
    # Convert response to json
    data = response.json()
    # Get relevant data
    price = data['data']['primaryData']['lastSalePrice']
    volume = data['data']['primaryData']['totalVolume']
    return price, volume

# Define function to pull real-time data from cryptocurrency exchanges
def get_crypto_data(symbol):
    # Construct API url
    url = 'https://api.coincap.io/v2/assets/{}'.format(symbol)
    # Make request
    response = requests.get(url)
    # Convert response to json
    data = response.json()
    # Get relevant data
    price = data['data']['priceUsd']
    return price

# Define function to calculate correlation between two