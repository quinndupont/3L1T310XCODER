

# Import necessary libraries
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

# Create a function to scrape data from the website
def scrape_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table containing the data
    table = soup.find('table')
    # Extract the table headers
    headers = [header.text for header in table.find_all('th')]
    # Extract the table rows
    rows = []
    for row in table.find_all('tr'):
        rows.append([data.text for data in row.find_all('td')])
    # Create a pandas dataframe with the extracted data
    df = pd.DataFrame(rows, columns=headers)
    # Drop the first row as it contains table headers again
    df.drop(0, inplace=True)
    # Reset the index
    df.reset_index(drop=True, inplace=True)
    # Return the dataframe
    return df

# Scrape data for Bhutan's cryptocurrency reserve
crypto_df = scrape_data('https://www.bhutan.gov.bt/government-reserve-cryptocurrency')

#