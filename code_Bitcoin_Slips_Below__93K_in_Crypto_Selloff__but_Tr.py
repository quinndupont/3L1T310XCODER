

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Obtain historical price data of Bitcoin from CoinMarketCap
df = pd.read_csv("https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20200101&end=20210331")

# Clean the data by removing any missing values or outliers
df = df.dropna()

# Calculate percentage change in Bitcoin's price over the past month
df["Pct Change"] = df["Close"].pct_change(periods=30)

# Create a line graph to visualize the price movement of Bitcoin over the past month
plt.plot(df["Date"], df["Close"])
plt.title("Bitcoin Price Movement")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.show()

# Identify the date and price at which Bitcoin slipped below $93K
below_93k = df[df["Close"] < 93000]
print("Date when Bitcoin slipped below $93K:", below_93k.iloc[0]["Date"])
print("Price when Bitcoin slipped below $93K:", below_93k.iloc[0]["Close"])

# Check if current price is below $93K and classify it as a "crypto selloff