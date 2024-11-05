

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Use requests library to retrieve historical data on Dogecoin and Bitcoin ETFs from a reliable source
dogecoin = requests.get('https://api.coingecko.com/api/v3/coins/dogecoin/market_chart?vs_currency=usd&days=90')
bitcoin = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=90')

# Convert the data into a pandas dataframe
dogecoin_df = pd.DataFrame(dogecoin.json()['prices'], columns=['date', 'dogecoin_price'])
bitcoin_df = pd.DataFrame(bitcoin.json()['prices'], columns=['date', 'bitcoin_price'])

# Clean and preprocess the data
dogecoin_df.drop_duplicates(inplace=True)
bitcoin_df.drop_duplicates(inplace=True)

# Merge the two dataframes on the date column
merged_df = pd.merge(dogecoin_df, bitcoin_df, on='date', how='outer')

# Create a line graph to visualize the historical performance of Dogecoin and Bitcoin ETFs leading up to the U.S. elections
plt.plot(merged_df['date'], merged