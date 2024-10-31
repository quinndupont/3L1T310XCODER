

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Retrieve and clean data for Bitcoin prices and ETF inflows
bitcoin_df = pd.read_csv("bitcoin_prices.csv") # Replace with the file path for the Bitcoin prices data
etf_df = pd.read_csv("etf_inflows.csv") # Replace with the file path for the ETF inflows data

# Calculate daily percentage change in Bitcoin prices and ETF inflows
bitcoin_df['Daily % Change'] = bitcoin_df['Price'].pct_change()
etf_df['Daily % Change'] = etf_df['Inflows'].pct_change()

# Plot a line graph to visualize the trend over time
plt.figure(figsize=(10,6))
plt.title("Bitcoin Prices and ETF Inflows over Time")
sns.lineplot(data=bitcoin_df, x="Date", y="Daily % Change", label="Bitcoin Price")
sns.lineplot(data=etf_df, x="Date", y="Daily % Change", label="ETF Inflows")
plt.xlabel("Date")
plt.ylabel("Daily % Change")
plt.legend()
plt.show()

# Calculate correlation coefficient and print the result
corr_coeff = bitcoin_df['Daily % Change