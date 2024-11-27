

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import re

# Use Coindesk API to retrieve latest headlines related to Tornado Cash
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(url)
data = response.json()

# Filter headlines to only include those mentioning the U.S. Appeals Court overturning sanctions against Tornado Cash
headlines = [headline['title'] for headline in data['bpi'] if 'U.S. Appeals Court' in headline['title']]

# Create function to extract date, time and percentage change from headlines
def extract_info(headline):
    # Use regular expressions to extract date and time
    datetime = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', headline).group()
    date = datetime.split(' ')[0]
    time = datetime.split(' ')[1]
    
    # Use regular expressions to extract percentage change
    change = re.search(r'\d+\.?\d*%', headline).group()
    percentage_change = float(change.strip('%'))
    
    return date