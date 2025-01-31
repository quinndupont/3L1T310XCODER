

# Import necessary libraries
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Define function to retrieve data from API
def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error retrieving data. Please check the URL.")

# Define function to calculate daily price changes
def get_daily_change(df):
    df['daily_change'] = df['price'].pct_change()
    return df

# Define function to calculate volatility
def get_volatility(df):
    df['volatility'] = df['price'].rolling(7).std()
    return df

# Define function to plot line graph of price changes
def plot_price_changes(df, currency):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=df['date'], y=df['price'], color='blue')
    plt.title(f"{currency} Price Changes in January", fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price', fontsize=12)
    plt.show()

# Define function to plot bar graph of