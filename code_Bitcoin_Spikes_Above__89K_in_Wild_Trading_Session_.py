

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Retrieve Bitcoin price data for specified time period
bitcoin_data = pd.read_csv("bitcoin_price_data.csv")

# Clean data by removing null values and duplicates
bitcoin_data.dropna(inplace=True)
bitcoin_data.drop_duplicates(inplace=True)

# Convert date column into datetime format
bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date'])

# Visualize the data using a line graph
plt.figure(figsize=(10,6))
plt.plot(bitcoin_data['Date'], bitcoin_data['Price'])
plt.title("Bitcoin Price Fluctuations")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.show()

# Calculate the percentage change in price
price_change = (bitcoin_data['Price'].iloc[-1] - bitcoin_data['Price'].iloc[0]) / bitcoin_data['Price'].iloc[0] * 100

# Print the percentage change in price
print("The percentage change in Bitcoin's price during the specified time period is: {:.2f}%".format(price_change))

# Identify the trading session based on the headline
if price_change > 0:
    print("The trading session was bullish.")
elif price_change < 0