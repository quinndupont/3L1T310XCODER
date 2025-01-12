

# Import necessary libraries
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# 1. Data Scraping
# Retrieve data from Coindesk about Bhutan's crypto reserve
url = "https://www.coindesk.com/bhutan-crypto-reserve/"
response = requests.get(url)

# Check if response is successful
if response.status_code == 200:
    print("Successfully retrieved data from Coindesk.")
else:
    print("Data retrieval failed.")

# Use BeautifulSoup to parse the HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant information (crypto reserve size and purpose)
crypto_reserve_size = soup.find("h2",{"class":"heading"}).get_text()
purpose = soup.find("p",{"class":"description"}).get_text()

# Print the retrieved information
print("Bhutan's crypto reserve size: " + crypto_reserve_size)
print("Purpose of the crypto reserve: " + purpose)

# 2. Sentiment Analysis
# Retrieve news articles and social media posts related to Bhutan's crypto reserve
news = "https://www.google.com/search