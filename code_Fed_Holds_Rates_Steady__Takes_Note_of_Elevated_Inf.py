

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Define function to gather data from Federal Reserve's website
def get_fed_data():
    # Define url to access data
    url = "https://www.federalreserve.gov/releases/h15/data.htm"
    # Send request to access data
    response = requests.get(url)
    # Convert response to dataframe
    df = pd.read_html(response.content)[1]
    # Clean up dataframe
    df.dropna(inplace=True)
    # Convert interest rates to numeric values
    df["Interest Rates"] = pd.to_numeric(df["Interest Rates"])
    # Return dataframe
    return df

# Define function to gather inflation data from FRED database
def get_inflation_data():
    # Define url to access data
    url = "https://fred.stlouisfed.org/series/CPIAUCSL"
    # Send request to access data
    response = requests.get(url)
    # Convert response to dataframe
    df = pd.read_html(response.content)[0]
    # Clean up dataframe
    df.dropna(inplace=True)
    # Convert dates to datetime format
    df["DATE"] = pd.to_datetime(df["DATE"])
   