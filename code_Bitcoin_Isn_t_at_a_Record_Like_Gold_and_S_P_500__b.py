

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# Define function to gather historical data
def get_historical_data(symbol):
    '''
    This function takes in a stock symbol and returns a dataframe with historical price data
    '''
    # Define base URL for Yahoo Finance API
    base_url = "https://query1.finance.yahoo.com/v7/finance/download/"

    # Define start and end dates for data retrieval
    start_date = '2015-01-01'
    end_date = '2020-12-31'

    # Make API call to retrieve historical data
    url = base_url + symbol + '?period1=' + start_date + '&period2=' + end_date + '&interval=1d&events=history&includeAdjustedClose=true'
    response = requests.get(url)

    # Convert response to dataframe
    df = pd.read_csv(response.text)

    # Set date as index
    df.set_index('Date', inplace=True)

    # Return dataframe
    return df

# Define function to gather news and events
def get_news(symbol):
    '''
    This function takes in a stock symbol and returns a