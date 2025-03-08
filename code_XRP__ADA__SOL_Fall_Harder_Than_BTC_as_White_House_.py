

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Get the data
# For this example, we will use Coindesk API to retrieve the price data
# of XRP, ADA, SOL, and BTC from the day of White House Crypto Summit until the current date
# Note: The API only allows 100 days of data at a time, so we will make multiple calls
# and combine the data into one dataframe
start_date = '2021-10-04' # White House Crypto Summit date
end_date = '2022-01-24' # Current date
base_url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start='

# Create a list of cryptocurrencies
cryptos = ['XRP', 'ADA', 'SOL', 'BTC']

# Create an empty dataframe to store the data
df = pd.DataFrame()

# Loop through the list of cryptocurrencies and retrieve the data
for crypto in cryptos:
    # Make API call and retrieve the data
    url = base_url + start_date + '&end=' + end_date + '&currency=' + crypto
    data = pd.read_json(url)['bpi