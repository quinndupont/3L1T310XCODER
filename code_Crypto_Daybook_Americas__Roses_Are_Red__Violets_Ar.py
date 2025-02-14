

# Import necessary libraries
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a function to retrieve data from reliable sources
def get_data():
    # Retrieve inflation data from government website
    infl_data = requests.get('https://www.bls.gov/cpi/data.htm').json()
    # Retrieve Bitcoin prices from cryptocurrency exchange
    btc_data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    # Return both data sets
    return infl_data, btc_data

# Define a function to calculate current inflation rate and average Bitcoin price in the Americas
def calculate_stats(infl_data, btc_data):
    # Extract inflation rate for Americas from data set
    infl_rates = infl_data['Americas']
    # Calculate average inflation rate
    avg_infl_rate = np.mean(infl_rates)
    # Extract Bitcoin price from data set
    btc_price = btc_data['bpi']['USD']['rate_float']
    # Return both calculated values
    return avg_infl_rate, btc_price

# Define a function to plot a graph of inflation rates and Bitcoin prices over a period of time
def plot_graph(infl_data, btc_data):
   