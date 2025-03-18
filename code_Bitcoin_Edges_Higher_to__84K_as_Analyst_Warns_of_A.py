

# Import necessary libraries
import requests
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Function to collect real-time data on the current price of Bitcoin
def get_bitcoin_data():
    # Make API request to Coindesk for current price of Bitcoin
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    # Extract current price from the response
    current_price = r['bpi']['USD']['rate_float']
    # Make API request to Coindesk for historical data of Bitcoin
    r = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-10-01&end=2021-10-31').json()
    # Extract historical data from the response
    historical_data = r['bpi']
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame.from_dict(historical_data, orient='index', columns=['USD Price'])
    # Add a column for date
    df['Date'] = df.index
    # Convert date column to datetime format
    df['Date'] = pd.to_datetime