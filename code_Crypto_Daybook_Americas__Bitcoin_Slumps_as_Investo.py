

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Collect historical price data for Bitcoin and gold
bitcoin_url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2020-01-01&end=2020-12-31'
gold_url = 'https://www.gold.org/api/price/USD'

bitcoin_data = pd.read_json(bitcoin_url)['bpi']
gold_data = pd.read_json(gold_url)['price']

# Preprocess the data
bitcoin_data = pd.DataFrame.from_dict(bitcoin_data, orient='index', columns=['Bitcoin Price'])
gold_data = pd.DataFrame(gold_data, columns=['Gold Price'])
bitcoin_data.index = pd.to_datetime(bitcoin_data.index)
gold_data['Date'] = pd.date_range('2020-01-01', '2020-12-31', freq='D')

# Merge the data frames
merged_data = pd.merge(bitcoin_data, gold_data, on='Date', how='inner')
merged_data = merged_data.set_index('Date')

# Visualize the data
merged_data.plot()
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Bitcoin vs Gold Price