

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Define function to gather data on ETFs performance and Bitcoin price
def get_data(start_date, end_date):
    # Read CSV file containing ETFs data
    etf_df = pd.read_csv('etf_data.csv')
    
    # Convert date column to datetime format
    etf_df['Date'] = pd.to_datetime(etf_df['Date'])
    
    # Filter data by start and end date
    etf_df = etf_df[(etf_df['Date'] >= start_date) & (etf_df['Date'] <= end_date)]
    
    # Read CSV file containing Bitcoin price data
    btc_df = pd.read_csv('btc_price.csv')
    
    # Convert date column to datetime format
    btc_df['Date'] = pd.to_datetime(btc_df['Date'])
    
    # Filter data by start and end date
    btc_df = btc_df[(btc_df['Date'] >= start_date) & (btc_df['Date'] <= end_date)]
    
    return etf_df, btc_df

# Define function to plot data in a line graph
def plot_data(etf