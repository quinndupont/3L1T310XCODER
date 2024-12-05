

# Import necessary libraries
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup

# Function to scrape data from cryptocurrency exchanges
def scrape_exchange_data():
    # Create a list of exchange URLs
    exchange_urls = ['https://www.coinbase.com/price/bitcoin', 'https://www.gemini.com/prices/bitcoin', 'https://bitso.com/trade/market/btc/mxn']

    # Create empty lists to store data
    prices = []
    volumes = []
    market_caps = []

    # Loop through each exchange URL
    for url in exchange_urls:
        # Make a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the elements with class 'PriceAmount'
        price = soup.find(class_='PriceAmount').text
        # Clean the price data and convert to float
        price = float(price.replace('$', '').replace(',', ''))
        # Add the price to the list
        prices.append(price)
        # Find the elements