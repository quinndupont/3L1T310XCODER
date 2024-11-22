

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# Set start and end date for data collection
start_date = '2021-11-01'
end_date = '2021-11-30'

# Define list of altcoins to track
altcoins = ['Bitcoin', 'Ethereum', 'Litecoin', 'Ripple', 'Cardano']

# Create empty dataframe to store altcoin prices
altcoin_df = pd.DataFrame()

# Loop through altcoins and collect data from Coinbase API
for altcoin in altcoins:
    # Construct API url
    url = f"https://api.coinbase.com/v2/prices/{altcoin}-USD/historic?start={start_date}&end={end_date}"
    # Make GET request
    response = requests.get(url)
    # Convert response to JSON format
    data = response.json()
    # Create dataframe from JSON data
    df = pd.DataFrame(data['data']['prices'], columns=['date', f'{altcoin}_price'])
    # Convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'])
    # Set date column as