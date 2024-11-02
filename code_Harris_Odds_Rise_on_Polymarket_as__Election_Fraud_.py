

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np

# Function to scrape data from Polymarket platform
def scrape_data():
    # URL for Harris Odds and Trump Hedge Bets
    url = 'https://polymarket.com/market/harris-odds'
    
    # Retrieve data from URL
    response = requests.get(url)
    
    # Create BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find Harris Odds and Trump Hedge Bets
    harris_odds = soup.find('div', {'class': 'sc-1b7o1w5-5 bTgLp'})
    trump_hedge_bets = soup.find('div', {'class': 'sc-1b7o1w5-5 bTgLp'})
    
    # Clean and format data
    harris_odds = float(harris_odds.text.replace('%', ''))
    trump_hedge_bets = float(trump_hedge_bets.text.replace('%', ''))
    
    return harris_odds, trump