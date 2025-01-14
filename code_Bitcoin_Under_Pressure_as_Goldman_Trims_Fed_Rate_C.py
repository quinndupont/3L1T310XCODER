

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Function to retrieve latest Bitcoin price data
def get_bitcoin_price():
    # Use CoinMarketCap API to get Bitcoin price data
    url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    response = requests.get(url)
    data = response.json()
    # Extract latest price
    price = float(data[0]['price_usd'])
    return price

# Function to collect latest news headlines related to Bitcoin
def get_bitcoin_news():
    # Use Coindesk as a source for Bitcoin news
    url = 'https://www.coindesk.com/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all headlines on the page
    headlines = soup.find_all('h3', class_='heading')
    # Create a list to store the headlines
    news = []
    # Loop through each headline and extract relevant information
    for headline in headlines:
        # Get the text of the headline
        title