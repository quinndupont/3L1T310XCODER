

# Import necessary libraries
import requests
import json
from datetime import datetime

# Function to get current Solana stablecoin supply from CoinMarketCap
def get_stablecoin_supply():
    # Make request to CoinMarketCap API
    response = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=solana&start=1&limit=100&sortBy=market_cap")
    # Convert response to JSON
    data = response.json()
    # Get current stablecoin supply
    stablecoin_supply = data["data"]["marketPairs"][0]["marketCap"]["totalSupply"]
    return stablecoin_supply

# Function to get current DEX volumes from Coingecko
def get_dex_volumes():
    # Make request to Coingecko API
    response = requests.get("https://api.coingecko.com/api/v3/coins/solana/dexes")
    # Convert response to JSON
    data = response.json()
    # Get current DEX volumes
    dex_volumes = data["tickers"][0]["converted_volume"]["usd"]
    return dex_volumes

# Function to calculate percentage increase
def calculate_percentage_increase(before, after):
   