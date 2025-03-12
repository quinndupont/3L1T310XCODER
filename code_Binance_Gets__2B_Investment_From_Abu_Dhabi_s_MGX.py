

# Import necessary libraries
import pandas as pd
import numpy as np
import requests
import json
import matplotlib.pyplot as plt
from textblob import TextBlob

# Retrieve and organize information on Binance's current financial status, past investments, and market share
# Get Binance's current financial status
binance_api_url = 'https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT'
binance_response = requests.get(binance_api_url)
binance_data = binance_response.json()

# Store relevant data in variables
binance_volume = float(binance_data['volume'])
binance_open_price = float(binance_data['openPrice'])
binance_close_price = float(binance_data['lastPrice'])
binance_market_cap = binance_volume * binance_close_price

# Get Binance's past investments
binance_investments_url = 'https://api.binance.com/api/v3/investment/project/summary'
binance_investments_response = requests.get(binance_investments_url)
binance_investments_data = binance_investments_response.json()

# Store relevant data in variables
binance_total_investments = binance_investments_data['totalInvestment']
