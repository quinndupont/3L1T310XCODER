

#Import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import matplotlib.pyplot as plt

#Make a GET request to the Coindesk article's URL and store the response in a variable
url = "https://www.coindesk.com/metaplanet-picks-up-record-620-bitcoin-as-xrp-leads-market-slide"
response = requests.get(url)

#Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

#Locate the section of the article that contains the market data
market_data = soup.find('div', class_='article-content')

#Extract the relevant data using regular expressions
btc_picked_up = re.findall(r'Metaplanet Picks Up Record (\d+) Bitcoin', market_data.text) #Amount of Bitcoin picked up by Metaplanet
xrp_value = re.findall(r'XRP at \$(\d+\.\d+)', market_data.text) #Current value of XRP

#Store the extracted data in variables
btc_picked_up = int(btc_picked_up[0])
xrp_value = float(xrp_value[0])

#Create a dataframe with the extracted data
df = pd