

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob

# Create a list of keywords
keywords = ['Bybit', 'Closes', 'ETH Gap', 'Exchange', 'Replenishes', '$1.4B', 'Hole', 'Hack']

# Use web scraping to gather data from Coindesk
url = 'https://www.coindesk.com/bybit-replenishes-1-4b-hole-after-hack'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Get the headline
headline = soup.find('h1').get_text()

# Get the date of the incident
date = soup.find('div', class_='timeauthor').get_text()

# Get the total amount stolen
amount_stolen = soup.find('div', class_='amount').get_text()

# Use web scraping to gather data from Bybit's official website
url = 'https://www.bybit.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Get the current