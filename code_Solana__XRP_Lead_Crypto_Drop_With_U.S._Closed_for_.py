

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datetime import datetime

# Task 1: Data Collection and Preparation
# Collecting data from Binance for Solana and XRP prices
solana_data = pd.read_csv('https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d')
xrp_data = pd.read_csv('https://api.binance.com/api/v3/klines?symbol=XRPUSDT&interval=1d')

# Cleaning and preparing data
solana_data = solana_data.drop(columns=['Open time', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
xrp_data = xrp_data.drop(columns=['Open time', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])

# Task 2: Identifying the Impact of U.S. Presidents' Day
# Collecting data on U.S. Presidents' Day dates
presidents_day_dates = pd.read_html('https://