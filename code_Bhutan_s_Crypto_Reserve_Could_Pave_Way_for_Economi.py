

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima_model import ARIMA

# Define function to scrape data from Coindesk
def scrape_coindesk():
    # Request page content
    page = requests.get('https://www.coindesk.com/')
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find the element with the latest crypto reserve value
    reserve_value = soup.find(class_ = 'price-large')
    # Convert the value to float
    reserve_value = float(reserve_value.text.strip().replace(',', ''))
    return reserve_value

# Define function to scrape data from CoinMarketCap
def scrape_coinmarketcap():
    # Request page content
    page = requests.get('https://coinmarketcap.com/')
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find the element with the latest crypto reserve value
    reserve_value = soup.find(class_ = 'cmc-link')
    # Convert the value to float
    reserve_value = float(reserve_value