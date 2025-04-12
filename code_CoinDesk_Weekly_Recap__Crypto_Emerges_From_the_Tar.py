

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data from the CoinDesk weekly recap article
crypto_data = pd.read_csv("crypto_market_data.csv")

# Check the data
crypto_data.head()

# Create a new column for the date in datetime format
crypto_data['Date'] = pd.to_datetime(crypto_data['Date'])

# Filter the data to only include dates before, during, and after the tariff war
before_tariff = crypto_data[crypto_data['Date'] < '2018-03-01']
during_tariff = crypto_data[(crypto_data['Date'] >= '2018-03-01') & (crypto_data['Date'] <= '2018-06-30')]
after_tariff = crypto_data[crypto_data['Date'] > '2018-06-30']

# Calculate the average performance of each cryptocurrency before, during, and after the tariff war
avg_before = before_tariff.mean()
avg_during = during_tariff.mean()
avg_after = after_tariff.mean()

# Create a bar chart to compare the average performance of each cryptocurrency before, during, and after the tariff war
plt.bar(x=['Bitcoin', 'Ethereum