

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# Function to scrape data from CoinMarketCap website
def scrape_data(url):
    # Request data from the URL
    response = requests.get(url)

    # Parse the data using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the desired data
    table = soup.find('table', {'class': 'cmc-table'})

    # Create a list to store the data
    data = []

    # Loop through each row in the table
    for row in table.find_all('tr'):
        # Get the data from each column in the row
        columns = row.find_all('td')
        # Check if the row is empty
        if len(columns) > 0:
            # Get the currency name
            name = columns[1].text.strip()
            # Get the price
            price = float(columns[3].text.strip().replace('$', '').replace(',', ''))
            # Get the market capitalization
            market_cap = float(columns[6].text.strip().replace('$', '').replace(',', ''))
            # Append the data to the