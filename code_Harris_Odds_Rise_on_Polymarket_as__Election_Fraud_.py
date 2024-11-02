
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# Load the data
df = pd.read_csv("coindesk_headline.csv")

# Clean the data
df['headline'] = df['headline'].str.replace('[^a-zA-Z0-9]', ' ') # Remove any special characters
df['headline'] = df['headline'].str.lower() # Convert to lowercase
df['headline'] = df['headline'].str.strip() # Remove leading and trailing spaces

# Extract relevant information
harris_odds = re.search(r'harris odds: (\d+)%', df['headline']).group(1) # Extract Harris' odds from the headline
polymarket = re.search(r'polymarket', df['headline']).group(0) # Extract Polymarket from the headline
election_fraud = re.search(r'election fraud', df['headline']).group(0) # Extract 'election fraud' allegations from the headline
trump_hedge_bets = re.search(r'trump hedge bets', df['headline']).group(0) # Extract Trump's hedge bets from the headline

# Perform sentiment analysis
def sentiment_analysis(headline):
   