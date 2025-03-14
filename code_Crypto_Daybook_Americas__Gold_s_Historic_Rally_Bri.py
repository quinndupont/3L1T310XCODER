

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Function to gather real-time data on gold and Bitcoin prices in the Americas region
def get_data():

    # Use requests library to get data from Coindesk API
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2020-01-01&end=2021-12-31&currency=USD'
    response = requests.get(url)

    # Convert data to JSON format
    data = response.json()

    # Create dataframes for gold and Bitcoin prices
    gold_df = pd.DataFrame(data['bpi']['GOLD'], index=['price']).T
    btc_df = pd.DataFrame(data['bpi']['BTC'], index=['price']).T

    # Return dataframes
    return gold_df, btc_df

# Function to plot a graph of gold and Bitcoin prices in the Americas region
def plot_graph(gold_df, btc_df):

    # Create a line plot for gold and Bitcoin prices
    plt.plot(gold_df.index, gold_df['price'], label='Gold')
    plt.plot(btc_df.index, btc_df['price