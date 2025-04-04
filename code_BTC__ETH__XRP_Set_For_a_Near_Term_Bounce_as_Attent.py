

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from CSV file
btc_data = pd.read_csv('btc_price_data.csv')
eth_data = pd.read_csv('eth_price_data.csv')
xrp_data = pd.read_csv('xrp_price_data.csv')
rate_cut_data = pd.read_csv('rate_cut_data.csv')

# Clean and prepare data
# Remove any irrelevant or duplicate data
btc_data = btc_data.drop_duplicates()
eth_data = eth_data.drop_duplicates()
xrp_data = xrp_data.drop_duplicates()
rate_cut_data = rate_cut_data.drop_duplicates()

# Convert data into usable format
# Convert date column to datetime format
btc_data['Date'] = pd.to_datetime(btc_data['Date'])
eth_data['Date'] = pd.to_datetime(eth_data['Date'])
xrp_data['Date'] = pd.to_datetime(xrp_data['Date'])
rate_cut_data['Date'] = pd.to_datetime(rate_cut_data['Date'])

# Merge different datasets based on date
combined_data = pd.merge(btc_data, eth_data, on='Date', how='outer')
combined_data = pd.merge(combined_data, xrp_data, on='Date', how='outer')
