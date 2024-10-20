

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import re
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Web scraping
url = 'https://www.coindesk.com/bitcoin-gold-sp500-overlooked-catalyst'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find headline and extract key information
headline = soup.find('h1').get_text()
bitcoin_mention = re.search(r'Bitcoin', headline)
gold_mention = re.search(r'gold', headline)
sp_mention = re.search(r'S&P 500', headline)

# Print key information
print(f"Bitcoin mentioned: {bitcoin_mention}")
print(f"Gold mentioned: {gold_mention}")
print(f"S&P 500 mentioned: {sp_mention}")

# Data cleaning and preprocessing
# Find all paragraphs in the article
paragraphs = soup.find_all('p')

# Extract text from paragraphs and convert it into a list
text = []
for p in paragraphs:
    text.append(p.get_text())

# Remove unnecessary characters and convert list