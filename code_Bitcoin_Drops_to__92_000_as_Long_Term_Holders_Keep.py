

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# Retrieve current Bitcoin price from Coindesk
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
current_price = response.json()['bpi']['USD']['rate_float']

# Gather historical price data from CoinMarketCap
historical_data = requests.get('https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1623465600&timeEnd=1628236800')
historical_data = historical_data.json()['data']['quotes']

# Create a dataframe with historical price data
df = pd.DataFrame(historical_data)
df['date'] = pd.to_datetime(df['timeClose'], unit='s')
df = df.set_index('date')

# Plot the historical price data
plt.figure(figsize=(10,6))
plt.plot(df['priceClose'], label='Bitcoin Price')
plt.title('Bitcoin Price Over the Past 3 Months')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Collect data on average holding period and percentage of Bitcoin held by long-term holders
