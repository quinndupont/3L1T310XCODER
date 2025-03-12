

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Function to gather data from Coindesk API
def get_coindesk_data(start_date, end_date):
    
    # Base URL for Coindesk API
    base_url = "https://api.coindesk.com/v1/bpi/historical/close.json"
    
    # Parameters for start and end date
    params = {"start": start_date, "end": end_date}
    
    # Make GET request to API with parameters
    response = requests.get(base_url, params=params)
    
    # Convert response to JSON format
    data = response.json()
    
    # Extract Bitcoin price data from JSON
    bitcoin_data = data["bpi"]
    
    # Convert data to Pandas DataFrame
    df = pd.DataFrame.from_dict(bitcoin_data, orient="index", columns=["Bitcoin Price (USD)"])
    
    # Return DataFrame
    return df

# Function to gather inflation data from FRED API
def get_inflation_data(start_date, end_date):
    
    # Base URL for FRED API
    base_url = "https://api.stlouisfed.org/fred/series/observations"
    
    # Parameters for