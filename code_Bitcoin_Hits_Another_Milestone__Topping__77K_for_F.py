

# Import necessary libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

# Define function to retrieve historical data from Coindesk API
def get_historical_data(start_date, end_date):
    # Set API endpoint and parameters
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
    params = {'start': start_date, 'end': end_date}
    
    # Send GET request and store response
    response = requests.get(url, params=params)
    
    # Convert response to JSON format
    data = json.loads(response.text)
    
    # Extract date and closing price data into lists
    dates = list(data['bpi'].keys())
    prices = list(data['bpi'].values())
    
    # Create a pandas dataframe from the data
    df = pd.DataFrame({'Date': dates, 'Closing Price': prices})
    
    # Convert date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set date column as index
    df.set_index('Date', inplace=True)
    
    return df

# Define function to retrieve funding rate data from Coindesk API
def get