

# Import necessary libraries
import pandas as pd             # For data manipulation and analysis
import numpy as np              # For mathematical calculations
import matplotlib.pyplot as plt # For data visualization
import requests                 # For making API requests
from datetime import datetime   # For working with date and time

# Set the API endpoints for cryptocurrency exchange platforms and foreign exchange websites
xrp_url = 'https://api.coinmarketcap.com/v1/ticker/xrp/'
btc_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
usd_url = 'https://api.exchangeratesapi.io/latest?base=USD'

# Function to get data from the API endpoints
def get_data(url):
    response = requests.get(url)  # Make a GET request to the API endpoint
    data = response.json()        # Convert the response to a JSON format
    return data[0]                # Return the first element of the JSON data

# Function to get percentage change in value over a specific time period
def get_percentage_change(current_value, previous_value):
    return (current_value - previous_value) / previous_value * 100

# Function to convert UNIX timestamp to a readable date
def convert_to_date(timestamp):
    return datetime