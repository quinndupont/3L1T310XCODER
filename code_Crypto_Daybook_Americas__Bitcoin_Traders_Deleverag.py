

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

# Define function to scrape data from website
def scrape_data(url):
    # Send request to URL and get response
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table with Bitcoin trading data
    table = soup.find('table', {'class': 'table'})
    # Get all rows from the table
    rows = table.find_all('tr')
    # Create empty lists to store data
    dates = []
    prices = []
    volumes = []
    sentiments = []
    # Loop through each row and extract data
    for row in rows[1:]:
        # Get all cells in the row
        cells = row.find_all('td')
        # Extract date, price, volume, and sentiment data
        date = cells[0].text
        price = float(cells[1].text.replace(',', ''))
        volume = float(cells[2].text.replace(',', ''))
        sentiment = float(cells[3].text)
        # Append data to respective lists
        dates