

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime

# Define function to gather data on cryptocurrency prices
def get_crypto_data(coin, start_date, end_date):
    # Define API endpoint and parameters
    endpoint = "https://api.coingecko.com/api/v3/coins/" + coin + "/market_chart/range"
    params = {"vs_currency": "usd", "from": start_date, "to": end_date}

    # Make API request and convert response to JSON format
    response = requests.get(endpoint, params=params)
    data = response.json()

    # Create lists to store data
    dates = []
    prices = []

    # Loop through data and extract desired values
    for item in data["prices"]:
        # Convert timestamp to datetime object
        date = datetime.fromtimestamp(item[0]/1000)
        # Append date and price to lists
        dates.append(date)
        prices.append(item[1])

    # Create pandas dataframe from lists
    df = pd.DataFrame({"Date": dates, coin.upper(): prices})

    return df

# Define function to gather data on news related to trade wars
def get_trade_war_news(start_date