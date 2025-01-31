

# Import necessary libraries
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Define function to collect data on current price trend of Bitcoin and other risk assets
def collect_data():
    # Make API call to get current Bitcoin price
    btc_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    btc_response = requests.get(btc_url)
    btc_data = btc_response.json()
    btc_price = btc_data['bpi']['USD']['rate_float']
    
    # Make API call to get current S&P 500 index price
    spx_url = "https://financialmodelingprep.com/api/v3/quotes/index?apikey=demo"
    spx_response = requests.get(spx_url)
    spx_data = spx_response.json()
    spx_price = spx_data[0]['price']
    
    # Make API call to get current gold price
    gold_url = "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?api_key=demo"
    gold_response = requests.get(gold_url)
    gold_data = gold_response