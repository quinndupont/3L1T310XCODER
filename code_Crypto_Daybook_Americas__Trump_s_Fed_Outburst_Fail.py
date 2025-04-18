

# Importing necessary libraries
import requests
import pandas as pd
from textblob import TextBlob

# Defining function to collect data on Bitcoin prices in the Americas
def get_bitcoin_data():
    # Making API call to Coindesk to get Bitcoin prices
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    # Converting response to JSON format
    bitcoin_data = response.json()

    # Extracting relevant data from the response
    date = bitcoin_data['time']['updated']
    time = bitcoin_data['time']['updatedISO']
    usd_price = bitcoin_data['bpi']['USD']['rate_float']
    cad_price = bitcoin_data['bpi']['CAD']['rate_float']
    mxn_price = bitcoin_data['bpi']['MXN']['rate_float']

    # Creating a dataframe to store the data
    df = pd.DataFrame({'Date': [date], 'Time': [time], 'USD Price': [usd_price], 'CAD Price': [cad_price], 'MXN Price': [mxn_price]})

    # Returning the dataframe
    return df

# Defining function to collect data on President Trump's remarks
def get_trump_remarks