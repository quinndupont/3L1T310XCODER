

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define function to collect data from Coindesk and Nasdaq
def collect_data():
    # Collect Bitcoin price data from Coindesk
    bitcoin_data = pd.read_csv('https://api.coindesk.com/v1/bpi/historical/close.json')
    # Convert date column to datetime format
    bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date'])
    
    # Collect Copper-Gold ratio data from Nasdaq
    copper_gold_data = pd.read_csv('https://www.nasdaq.com/api/v1/historical/CU-AU-RATIO')
    # Convert date column to datetime format
    copper_gold_data['Date'] = pd.to_datetime(copper_gold_data['Date'])
    
    return bitcoin_data, copper_gold_data

# Define function to clean and prepare data for analysis
def clean_data(bitcoin_data, copper_gold_data):
    # Drop any missing values
    bitcoin_data.dropna(inplace=True)
    copper_gold_data.dropna(inplace=True)
    
    # Convert Bitcoin price to USD
    bitcoin_data['Close'] = bitcoin_data['Close'] * 1000
    
    # Merge Bitcoin and Copper