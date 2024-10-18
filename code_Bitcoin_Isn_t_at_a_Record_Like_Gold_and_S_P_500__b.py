

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Obtain historical data for Bitcoin, Gold, and S&P 500 from Yahoo Finance
bitcoin_df = pd.read_csv("https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1588291200&period2=1620576000&interval=1d&events=history&includeAdjustedClose=true")
gold_df = pd.read_csv("https://query1.finance.yahoo.com/v7/finance/download/GC=F?period1=1588291200&period2=1620576000&interval=1d&events=history&includeAdjustedClose=true")
sp500_df = pd.read_csv("https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=1588291200&period2=1620576000&interval=1d&events=history&includeAdjustedClose=true")

# Clean the data by removing null values and outliers
bitcoin_df.dropna(inplace=True)
gold_df.dropna(inplace=True)
sp500_df.dropna(inplace=True)

# Use descriptive statistics to get an overall understanding of the data