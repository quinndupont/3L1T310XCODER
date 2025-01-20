

# Import necessary libraries
import requests
import json
import time
import matplotlib.pyplot as plt

# Define function to retrieve latest price data from reputable cryptocurrency exchanges
def get_price_data(coin):
    # Define API endpoint for Solana and Official Trump Memecoin
    if coin == "Solana":
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    elif coin == "Official Trump Memecoin":
        url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-01-01&end=2021-10-31"
    else:
        print("Invalid coin name.")
        return None
    
    # Send GET request to API endpoint and store response
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code == 200:
        # Convert response to JSON format and store data
        data = json.loads(response.content)
        
        # Retrieve latest price data
        if coin == "Solana":
            price = data["bpi"]["USD"]["rate_float"]
            date = data["time"]["updated"]
        elif coin == "Official Trump Memecoin":
            price = max(data