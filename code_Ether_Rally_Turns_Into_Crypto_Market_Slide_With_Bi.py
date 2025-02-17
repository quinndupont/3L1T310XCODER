

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gather data from Coindesk and CoinMarketCap
ether_data = pd.read_csv('https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-01-01&end=2021-04-30')
bitcoin_data = pd.read_csv('https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-01-01&end=2021-04-30')
ether_price = ether_data['bpi'].values
bitcoin_price = bitcoin_data['bpi'].values

# Calculate correlation coefficient
corr = np.corrcoef(ether_price, bitcoin_price)[0, 1]

# Print correlation coefficient
print("Correlation coefficient between Ether and Bitcoin prices: ", corr)

# Visualize the relationship between the two cryptocurrencies using a scatter plot
plt.scatter(ether_price, bitcoin_price)
plt.xlabel("Ether Price")
plt.ylabel("Bitcoin Price")
plt.title("Correlation between Ether and Bitcoin Prices")
plt.show()

# Determine the direction of the relationship using a heatmap
data = {'Ether': ether_price, 'Bitcoin':