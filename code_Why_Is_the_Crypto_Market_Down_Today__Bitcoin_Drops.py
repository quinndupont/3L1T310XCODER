 

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to scrape data from CoinMarketCap
def get_data(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table element containing the data we want
    table = soup.find('table', {'class': 'cmc-table'})
    # Extract the table headers
    headers = [header.text for header in table.find_all('th')]
    # Extract the table rows
    rows = []
    for row in table.find_all('tr'):
        rows.append([val.text.strip() for val in row.find_all('td')])

    # Remove the first row as it contains empty values
    rows = rows[1:]
    # Create a dataframe with the extracted data
    df = pd.DataFrame(rows, columns=headers)
    # Convert the 'Price' column to a numeric datatype
    df['Price'] = pd.to_numeric(df['Price'].str.replace(',', '').str.replace('$', ''))
    # Convert the