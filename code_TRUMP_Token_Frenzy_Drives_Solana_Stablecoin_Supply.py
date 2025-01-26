

# Import necessary libraries
import requests # for making HTTP requests
import json # for handling JSON data
import pandas as pd # for data manipulation and analysis

# Define function to gather data on Solana stablecoin supply
def get_solana_supply():
    # Make HTTP request to Coindesk API
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # Convert response to JSON format
    data = r.json()
    # Get current supply of Solana stablecoin from JSON data
    solana_supply = data['bpi']['USD']['rate_float']
    # Return current supply
    return solana_supply

# Define function to track Solana stablecoin supply growth over time
def track_solana_supply_growth():
    # Make HTTP request to Coindesk API
    r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-01-01&end=2021-12-31')
    # Convert response to JSON format
    data = r.json()
    # Create dataframe from JSON data
    df = pd.DataFrame.from_dict(data['bpi'], orient='index', columns=['Closing Price'])
    #