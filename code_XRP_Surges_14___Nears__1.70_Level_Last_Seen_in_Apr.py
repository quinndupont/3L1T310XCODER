

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Define function to retrieve data from Coindesk's API
def get_data():
    # Define API endpoint and parameters
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
    params = {'start': '2021-04-01', 'end': '2021-05-10', 'currency': 'USD'}
    
    # Make GET request to API
    response = requests.get(url, params=params)
    
    # Convert response to JSON format
    data = response.json()
    
    # Extract relevant data from JSON
    prices = data['bpi']
    
    # Convert data to dataframe
    df = pd.DataFrame.from_dict(prices, orient='index', columns=['Price'])
    
    return df

# Define function to calculate percentage change
def calculate_change(df):
    # Calculate percentage change from previous level to $1.70
    prev_level = df.iloc[-1]['Price']
    current_level = 1.70
    change = ((current_level - prev_level) / prev_level) * 100
    
    return change

# Define