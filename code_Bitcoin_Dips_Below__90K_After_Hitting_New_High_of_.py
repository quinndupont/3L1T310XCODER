

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Bitcoin price data
bitcoin_data = pd.read_csv('bitcoin_prices.csv')

# Load Nasdaq-to-S&P 500 ratio data
nasdaq_snp_data = pd.read_csv('nasdaq_snp_ratio.csv')

# Check data
print(bitcoin_data.head())
print(nasdaq_snp_data.head())

# Merge the two datasets on date
merged_data = pd.merge(bitcoin_data, nasdaq_snp_data, on='Date')

# Check merged data
print(merged_data.head())

# Calculate correlation coefficient
corr_coeff = merged_data['Bitcoin Price'].corr(merged_data['Nasdaq-to-S&P 500 Ratio'])

# Print correlation coefficient
print("The correlation coefficient between Bitcoin price and Nasdaq-to-S&P 500 ratio is:", corr_coeff)

# Visualize the relationship between the two variables
sns.scatterplot(x='Nasdaq-to-S&P 500 Ratio', y='Bitcoin Price', data=merged_data)
plt.title('Bitcoin Price vs Nasdaq-to-S&P 500 Ratio')
plt.xlabel('Nasdaq-to-S&P 500 Ratio')
plt.ylabel('Bitcoin Price')
plt