

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data from StanChart
# Assume data is already cleaned and saved as csv files
mag7_returns = pd.read_csv('mag7_returns.csv') # Historical returns of the Mag 7 companies
bitcoin_prices = pd.read_csv('bitcoin_prices.csv') # Historical prices of Bitcoin
tesla_prices = pd.read_csv('tesla_prices.csv') # Historical prices of Tesla
mag7_financials = pd.read_csv('mag7_financials.csv') # Relevant financial data of the Mag 7 companies

# Calculate returns of Mag 7 companies
# Returns are calculated using the formula: (Ending Price - Beginning Price) / Beginning Price
mag7_returns['Company 1 Returns'] = (mag7_returns['Company 1 Ending Price'] - mag7_returns['Company 1 Beginning Price']) / mag7_returns['Company 1 Beginning Price']
mag7_returns['Company 2 Returns'] = (mag7_returns['Company 2 Ending Price'] - mag7_returns['Company 2 Beginning Price']) / mag7_returns['Company 2 Beginning Price']
mag7_returns['Company 3 Returns']