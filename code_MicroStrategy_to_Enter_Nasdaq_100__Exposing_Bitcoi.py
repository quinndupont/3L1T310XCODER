

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Obtain dataset of historical stock prices
msft_df = pd.read_csv('msft_stock_prices.csv') # MicroStrategy's stock prices
btc_df = pd.read_csv('btc_stock_prices.csv') # Bitcoin-linked stock prices
nasdaq_df = pd.read_csv('nasdaq100_index.csv') # Nasdaq 100 index prices

# Clean and preprocess the data
msft_df['Date'] = pd.to_datetime(msft_df['Date']) # Convert Date column to datetime format
msft_df = msft_df.dropna() # Drop any rows with missing values

btc_df['Date'] = pd.to_datetime(btc_df['Date'])
btc_df = btc_df.dropna()

nasdaq_df['Date'] = pd.to_datetime(nasdaq_df['Date'])
nasdaq_df = nasdaq_df.dropna()

# Create a line graph for MicroStrategy's stock price over time
plt.plot(msft_df['Date'], msft_df['Close'])
plt.title('MicroStrategy Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.show()

# Create a scatter plot for MicroStrategy's stock price and Bitcoin