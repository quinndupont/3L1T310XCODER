

# Import necessary libraries
import requests
import json

# Define function to retrieve and store current prices from cryptocurrency data source
def get_current_prices():
    # Use Coindesk API to retrieve current Bitcoin price
    bitcoin_response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # Check for successful response
    if bitcoin_response.status_code == 200:
        # Store current Bitcoin price in a variable
        bitcoin_price = bitcoin_response.json()['bpi']['USD']['rate_float']
    else:
        # Display error message if API call fails
        print('Error: Unable to retrieve Bitcoin price from Coindesk API.')
        return None
    
    # Use Coingecko API to retrieve current Ether and XRP prices
    coingecko_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum%2Cxrpl&vs_currencies=usd')
    # Check for successful response
    if coingecko_response.status_code == 200:
        # Store current Ether and XRP prices in variables
        ether_price = coingecko_response.json()['ethereum']['usd']
        xrp_price = coingecko_response.json()['xrpl