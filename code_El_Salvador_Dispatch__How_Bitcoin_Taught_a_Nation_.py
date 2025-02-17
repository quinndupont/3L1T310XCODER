

# Import necessary libraries
import pandas as pd
import numpy as np
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# Define function to gather data on Bitcoin adoption in El Salvador
def get_bitcoin_data():
    # API endpoint for Bitcoin data in El Salvador
    url = "https://api.alternative.me/v2/ticker/bitcoin/?convert=USD&limit=1"
    
    # Make GET request to the API and store response
    response = requests.get(url)
    
    # Convert response to JSON format
    data = response.json()
    
    # Extract relevant data from JSON
    bitcoin_price = data["data"]["1"]["quotes"]["USD"]["price"]
    bitcoin_market_cap = data["data"]["1"]["quotes"]["USD"]["market_cap"]
    bitcoin_volume = data["data"]["1"]["quotes"]["USD"]["volume_24h"]
    
    # Return data as a dictionary
    return {"Price": bitcoin_price, "Market Cap": bitcoin_market_cap, "Volume (24h)": bitcoin_volume}

# Define function to gather data on Bitcoin adoption in El Salvador
def get_el_salvador_data():
    # API endpoint for El Salvador data