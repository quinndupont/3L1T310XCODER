

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Define function to collect data from exchanges
def data_collection():
    # Create list of exchanges to gather data from
    exchanges = ['Coinbase', 'Binance', 'Kraken']
    
    # Create empty dataframe to store data
    df = pd.DataFrame()
    
    # Loop through exchanges
    for exchange in exchanges:
        # Read data from exchange
        data = pd.read_csv(exchange + '_data.csv')
        
        # Add exchange name as column
        data['Exchange'] = exchange
        
        # Append data to main dataframe
        df = df.append(data, ignore_index=True)
    
    # Return dataframe
    return df

# Define function to visualize data
def data_visualization(data):
    # Create line graph of Bitcoin price based on date
    plt.plot(data['Date'], data['Price'])
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Bitcoin Price Trend')
    plt.show()

# Define function to analyze data
def price_analysis(data):
    # Calculate mean price
    mean_price