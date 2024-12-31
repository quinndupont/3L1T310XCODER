

# Import necessary libraries
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Retrieve data on BTC ETFs from CoinGecko
btc_etf_data = pd.read_csv('https://api.coingecko.com/api/v3/coins/bitcoin?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false')

# Clean the data by removing irrelevant columns and handling missing values
btc_etf_data = btc_etf_data.drop(['community_score', 'developer_score', 'public_interest_score'], axis=1)
btc_etf_data = btc_etf_data.replace('-', np.nan).dropna()

# Calculate total amount lost in BTC ETFs
total_lost = btc_etf_data.iloc[0]['market_cap'] - btc_etf_data.iloc[1]['market_cap']

# Perform sentiment analysis on headline using NLTK
headline = 'BTC ETFs experience significant drop, causing concern for Bitcoin market'
sid = SentimentIntensityAnalyzer()
sentiment_scores = sid.polarity_scores(headline)
sentiment = sentiment_scores['compound']

# Extract key phrases and keywords from headline
tokens = nltk.word_tokenize