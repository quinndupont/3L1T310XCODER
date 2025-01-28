

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define function to retrieve list of cryptocurrencies supported by Coinbase
def get_supported_currencies():
    # Make API call to Coinbase
    response = requests.get("https://api.coinbase.com/v2/currencies")
    # Convert response to JSON format
    data = response.json()
    # Retrieve list of currencies from JSON data
    currencies = data['data']
    # Create empty list to store supported currencies
    supported_currencies = []
    # Loop through currencies and add to supported currencies list
    for currency in currencies:
        supported_currencies.append(currency['id'])
    # Return supported currencies list
    return supported_currencies

# Define function to retrieve current market value of each cryptocurrency
def get_market_value(currencies):
    # Create empty dictionary to store market values
    market_values = {}
    # Loop through currencies
    for currency in currencies:
        # Make API call to cryptocurrency exchange or aggregator
        response = requests.get("https://api.coinmarketcap.com/v1/ticker/" + currency)
        # Convert response to JSON format
        data = response.json()
        # Retrieve market value from JSON data
        market_value = data[0]['price_us