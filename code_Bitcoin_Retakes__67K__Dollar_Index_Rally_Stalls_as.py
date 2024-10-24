

# Import necessary libraries
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# Retrieve data from Coindesk API
bitcoin_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(bitcoin_url)
bitcoin_data = response.json()

# Retrieve data from Federal Reserve's Beige Book report
beigebook_url = "https://www.federalreserve.gov/monetarypolicy/beigebook2021.htm"
beigebook_response = requests.get(beigebook_url)
beigebook_data = beigebook_response.text

# Store relevant data from Coindesk API
bitcoin_price = bitcoin_data['bpi']['USD']['rate_float']

# Store relevant data from Federal Reserve's Beige Book report
beigebook_list = beigebook_data.split('\n\n')
beigebook_headline = beigebook_list[2]
beigebook_decision = beigebook_list[3]

# Calculate price movements
bitcoin_movement = bitcoin_price - bitcoin_data['bpi']['USD']['yesterday_rate_float']

# Print analysis
print("The price of Bitcoin is currently at ${}.".format(bitcoin_price))
print("The Federal Reserve's Beige Book report headline is: {}".format