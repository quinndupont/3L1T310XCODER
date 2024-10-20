

# Import necessary libraries
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from ta import *
from ta.utils import dropna
from statsmodels.tsa.stattools import coint

# Define the time period for data collection
start = dt.datetime(2015,1,1)
end = dt.datetime.now()

# Retrieve and compile historical data for Bitcoin, Gold, and S&P 500
btc = web.DataReader('BTC-USD', 'yahoo', start, end) # Bitcoin
gold = web.DataReader('GC=F', 'yahoo', start, end) # Gold
snp = web.DataReader('^GSPC', 'yahoo', start, end) # S&P 500

# Calculate and plot the trends and patterns of each asset
fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(10,10))

# Plot Bitcoin
ax1.plot(btc['Adj Close'])
ax1.set_title('Bitcoin Price')
ax1.set_ylabel('Price ($)')

# Plot Gold
ax2.plot(gold['Adj Close'])
ax2.set_title('Gold Price')
ax2