

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Define function to scrape data from popular exchanges
def get_data(coin, exchange):
    """
    This function takes in a cryptocurrency and exchange as parameters and scrapes real-time price data from the exchange's website.
    It returns a dataframe with the date and price data for the specified cryptocurrency.
    """
    # Construct URL for the specific cryptocurrency and exchange
    url = f'https://www.{exchange}.com/price/{coin}-usd'
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the table containing the price data
    table = soup.find('table', class_='data-table')
    # Extract the date and price data from the table
    dates = [date.text for date in table.find_all('td', class_='text-right')]
    prices = [price.text for price in table.find_all('td', class_='text-left')]
    # Create a dataframe with the date and price data
    df