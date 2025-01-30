

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import datetime

# Function to collect data from various sources
def data_collection():
    # Cryptocurrency market data
    # Use CoinMarketCap API to retrieve data for cryptocurrencies in the Americas
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit=100'

    # Make API call and store response in a variable
    response = requests.get(url)

    # Convert response into JSON format
    data = response.json()

    # Store data in a Pandas DataFrame for easier analysis
    df = pd.DataFrame(data)

    # News data
    # Use News API to retrieve news articles related to cryptocurrencies in the Americas
    news_url = 'https://newsapi.org/v2/everything?q=cryptocurrency&domains=cointelegraph.com,coindesk.com&from=2019-02-19&sortBy=publishedAt&apiKey=YOUR_API_KEY'

    # Make API call and store response in a variable
    news_response = requests.get(news_url)

    # Convert response into JSON format
    news_data = news_response.json()

    # Store data in a