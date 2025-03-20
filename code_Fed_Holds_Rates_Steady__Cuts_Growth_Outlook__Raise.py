

# Import necessary libraries
import requests
import re
import matplotlib.pyplot as plt
import numpy as np

# Define function to extract relevant data from Coindesk headline
def extract_data(headline):
    # Use regular expressions to find key actions
    actions = re.findall(r'Holds Rates Steady|Cuts Growth Outlook|Raises Inflation Forecast', headline)
    # Use regular expressions to find current interest rate
    current_rate = float(re.search(r'\d+\.\d+', headline).group())
    # Use regular expressions to find previous interest rate
    previous_rate = float(re.search(r'\d+\.\d+', headline.split(',')[0]).group())
    # Use regular expressions to find latest growth outlook
    latest_growth = float(re.search(r'\d+\.\d+', headline.split(',')[1]).group())
    # Use regular expressions to find previous growth outlook
    previous_growth = float(re.search(r'\d+\.\d+', headline.split(',')[2]).group())
    # Use regular expressions to find latest inflation forecast
    latest_inflation = float(re.search(r'\d+\.\d+', headline.split(',')[3]).group())
    # Use regular expressions to find previous inflation forecast
    previous_inflation = float(re.search(r'\d