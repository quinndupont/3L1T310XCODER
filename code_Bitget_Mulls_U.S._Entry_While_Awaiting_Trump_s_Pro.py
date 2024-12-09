

# Import necessary libraries
import pandas as pd
import numpy as np
import requests
import nltk
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Data Gathering
# Gather data on current policies and actions of the Trump administration towards cryptocurrencies
# API call to CoinMarketCap for Bitcoin price data
api_key = 'insert your API key here'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {'symbol': 'BTC'}
headers = {'X-CMC_PRO_API_KEY': api_key}
response = requests.get(url, headers=headers, params=parameters).json()

# Store data in a dataframe
btc_df = pd.DataFrame(response['data']['BTC']['quote']['USD'], index=[0])

# Sentiment Analysis
# Perform sentiment analysis on relevant news articles and social media posts
# Get dataset of tweets containing "Trump" and "cryptocurrency"
twitter_df = pd.read_csv('https://raw.githubusercontent.com/abhijeetdtu/cryptocurrency-twitter-analysis/master/twitter_bitcoin.csv')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Create a new column for sentiment analysis scores
twitter_df['Sentiment Score'] =