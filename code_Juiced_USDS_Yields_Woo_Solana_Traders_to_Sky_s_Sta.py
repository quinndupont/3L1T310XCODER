

# Import necessary libraries
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to get USDS yields data from Coingecko
def get_usds_yields():
    # Make API call to Coingecko
    response = requests.get('https://api.coingecko.com/api/v3/coins/solana/contract/0x9a9d1a69b73b2d2423fbc563f4b4fae7aef1c0f6')
    data = response.json()
    
    # Get only the relevant data for USDS yields
    usds_data = data['tickers'][0]['converted_last']['usd']
    
    return usds_data

# Function to get Solana trading volume data from Coinmarketcap
def get_solana_trading_volume():
    # Make API call to Coinmarketcap
    response = requests.get('https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=solana&start=1&limit=100&sortBy=volume&sortType=desc&convertId=2781&aux=ath,atl,market_cap,details,id,rank