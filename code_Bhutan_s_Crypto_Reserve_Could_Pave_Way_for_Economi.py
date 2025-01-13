

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Gather data from government reports and cryptocurrency market data
gov_report = pd.read_csv('bhutan_economic_growth.csv') # government report on Bhutan's economic growth
crypto_data = pd.read_csv('crypto_market_data.csv') # cryptocurrency market data

# Data cleaning and preprocessing
# Drop irrelevant columns and rename columns for easier analysis
gov_report = gov_report.drop(['Year'], axis=1)
gov_report = gov_report.rename(columns={'GDP_growth': 'Bhutan_GDP_growth'})

# Merge the two datasets on the year column
merged_data = pd.merge(gov_report, crypto_data, on='Year')

# Calculate the percentage change of Bhutan's GDP growth and crypto market growth
merged_data['Bhutan_GDP_growth_pct'] = merged_data['Bhutan_GDP_growth'].pct_change()
merged_data['Crypto_market_growth_pct'] = merged_data['Market_cap'].pct_change()

# Hypothesis testing
# Null hypothesis: There is no significant relationship between Bhutan's crypto reserve and economic growth in other countries.
# Alternative hypothesis: There is a