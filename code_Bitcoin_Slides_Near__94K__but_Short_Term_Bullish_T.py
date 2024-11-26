

# Import necessary libraries
import requests
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Retrieve current price of Bitcoin from Coindesk
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = r.json()
current_price = data['bpi']['USD']['rate']

# Calculate percentage change in price compared to previous day
# Retrieve previous day's price from Coindesk
yesterday = datetime.date.today() - datetime.timedelta(days=1)
yesterday = yesterday.strftime("%Y-%m-%d")
r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start='+yesterday+'&end='+yesterday)
data = r.json()
previous_price = data['bpi'][yesterday]

# Calculate percentage change
percent_change = ((float(current_price.replace(',','')) - previous_price)/previous_price)*100

# Identify if current price is below or above the short-term bullish target of $100K
bullish_target = 100000
if float(current_price.replace(',','')) < bullish_target:
    # Calculate percentage difference
    percent_difference = ((bullish_target - float(current_price.replace(',','')))/bullish_target