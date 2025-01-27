

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Use Coindesk API to retrieve data from article
coindesk_url = "https://www.coindesk.com/trump-token-frenzy-solana-stablecoin-supply-dex-volumes"
df = pd.read_html(coindesk_url)[0]

# Convert data into pandas dataframe
df = pd.DataFrame(df)

# Clean data
df.drop(columns=["Unnamed: 0"], inplace=True) # Remove irrelevant column
df.dropna(inplace=True) # Remove rows with missing values

# Descriptive statistics
print("Stablecoin Supply Stats:")
print("Mean: ", df["Stablecoin Supply"].mean())
print("Median: ", df["Stablecoin Supply"].median())
print("Std Dev: ", df["Stablecoin Supply"].std())
print()
print("DEX Volumes Stats:")
print("Mean: ", df["DEX Volumes"].mean())
print("Median: ", df["DEX Volumes"].median())
print("Std Dev: ", df["DEX Volumes"].std())

# Visualize data
plt.plot(df["Date"], df["Stablecoin Supply"])
plt.xlabel("Date")
plt.ylabel("