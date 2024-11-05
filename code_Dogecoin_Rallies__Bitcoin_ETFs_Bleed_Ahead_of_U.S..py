

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import yfinance as yf

# Function to get historical price data for a given asset and time period
def get_price_data(asset, start_date, end_date):
    ticker = yf.Ticker(asset)
    data = ticker.history(start=start_date, end=end_date)
    return data

# Function to calculate percentage change
def calculate_percentage_change(df):
    return df.pct_change()

# Function to calculate volatility
def calculate_volatility(df):
    return df.std()

# Function to calculate trading volume
def calculate_trading_volume(df):
    return df['Volume'].mean()

# Function to plot the price trend of an asset
def plot_price_trend(df, asset_name):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label=asset_name)
    plt.title(asset_name + ' Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

# Function to plot the percentage change of an asset
def plot_percentage_change(df, asset_name):
    plt.figure(figsize=(12, 6))
