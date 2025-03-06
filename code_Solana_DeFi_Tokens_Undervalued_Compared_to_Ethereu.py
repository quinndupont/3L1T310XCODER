

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define function to scrape data from Coindesk article
def scrape_data(url):
    # Make GET request to the URL
    response = requests.get(url)
    # Check if response is successful
    if response.status_code == 200:
        # Get the HTML content from the response
        html = response.content
        # Use pandas to read the HTML table
        df = pd.read_html(html)[0]
        # Return the data frame
        return df
    else:
        # Print error message if request is unsuccessful
        print("Error: Unable to fetch data from URL")

# Define function to clean and preprocess data
def clean_data(df):
    # Drop unnecessary columns
    df = df.drop(['Date', '1-Day Change'], axis=1)
    # Rename columns
    df.columns = ['Token', 'Price (USD)', 'Market Cap (USD)', 'Market Cap %']
    # Convert Price and Market Cap columns to float
    df['Price (USD)'] = df['Price (USD)'].str.replace('$', '').astype(float)
    df['Market Cap (USD)'] = df['Market Cap