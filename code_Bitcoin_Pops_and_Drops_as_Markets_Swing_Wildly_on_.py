

# Import necessary libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from textblob import TextBlob

# Retrieve the latest tariff news from Coindesk
url = 'https://www.coindesk.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
tariff_news = soup.find('h3', class_='heading').text

# Use web scraping to extract current value of Bitcoin from Coinbase
url = 'https://www.coinbase.com/price/bitcoin'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
bitcoin_value = soup.find('span', class_='AssetPrice').text

# Convert Bitcoin value to float
bitcoin_value = float(bitcoin_value.replace(',', ''))

# Compare current value with previous value and calculate percentage change
previous_bitcoin_value = 10000 # Assuming the previous value was $10,000
percentage_change = (bitcoin_value - previous_bitcoin_value) / previous_bitcoin_value * 100

# Analyze the tariff news for potential impact on the market
keywords = ['tariff', 'trade war', 'import', 'export']
tariff_impact = False
for keyword in keywords:
