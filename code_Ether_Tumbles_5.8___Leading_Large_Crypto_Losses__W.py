

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

# Use web scraping to extract data from Coindesk article
url = 'https://www.coindesk.com/ether-tumbles-5-8-leading-large-crypto-losses-with-bitcoin-sliding-below-71k'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Create dataframe to store data
df = pd.DataFrame(columns=['Date', 'Ether Price', 'Bitcoin Price'])

# Extract data from article and add to dataframe
dates = soup.find_all('time', class_='time')
ether_prices = soup.find_all('span', class_='price-medium')
bitcoin_prices = soup.find_all('span', class_='price-large')

for i in range(len(dates)):
    date = dates[i].get_text()
    ether_price = ether_prices[i].get_text()
    bitcoin_price = bitcoin_prices[i].get_text()
    df.loc[i] = [date, ether_price, bitcoin_price]

# Clean data and convert to numerical values
df['Ether Price'] = df['Ether Price'].str.replace('$', '').str.replace(',', '').astype(float)
df['