

# Import necessary libraries
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Scrape data from Coindesk
url = "https://www.coindesk.com/price/bitcoin"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data from relevant sources
price_data = soup.find('div', {'class': 'price-large'}).find('div', {'class': 'price-large'}).text
market_cap = soup.find('div', {'class': 'price-large'}).find('div', {'class': 'price-large'}).find_next_sibling('div').text
market_share = soup.find('div', {'class': 'price-large'}).find('div', {'class': 'price-large'}).find_next_sibling('div').find_next_sibling('div').text
volume = soup.find('div', {'class': 'price-large'}).find('div', {'class': 'price-large'}).find_next_sibling('div').find_next_sibling('div').find_next_sibling('div').text

# Convert data to appropriate format
price_data = float(price_data.strip('$').replace(',', ''))
market_cap = float(market_cap.strip('$').replace