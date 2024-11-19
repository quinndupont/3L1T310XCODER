

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datetime import datetime

# Define function to get Bitcoin price data from Coindesk API
def get_bitcoin_data():
    # URL for Coindesk API
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2010-07-17&end=2021-07-17'

    # Get response from API
    response = requests.get(url)

    # Convert response to JSON format
    data = response.json()

    # Extract relevant data from JSON
    dates = list(data['bpi'].keys())
    prices = list(data['bpi'].values())

    # Create dataframe with extracted data
    df = pd.DataFrame({'Date': dates, 'Price': prices})

    # Convert date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    return df

# Define function to get ETF launch dates and associated prices from CSV file
def get_etf_data():
    # Read CSV file into dataframe
    df = pd.read_csv('etf_data.csv')

    # Convert date column to datetime format
    df