

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Gather data
bitcoin_data = pd.read_csv("bitcoin_price_data.csv") # dataset containing Bitcoin price data
accounting_rule_data = pd.read_csv("accounting_rule_data.csv") # dataset containing information on the implementation of the new accounting rule in the Americas region

# Step 2: Data cleaning
# Check for duplicates
print("Number of duplicate values in Bitcoin price data: ", bitcoin_data.duplicated().sum())
print("Number of duplicate values in accounting rule data: ", accounting_rule_data.duplicated().sum())

# Fill in missing values
bitcoin_data = bitcoin_data.fillna(method='ffill') # forward fill the missing values
accounting_rule_data = accounting_rule_data.fillna(method='bfill') # backward fill the missing values

# Correct errors
# Check for outliers in Bitcoin price data
sns.boxplot(x=bitcoin_data['Price'])
plt.show()

# We can see that there are some outliers in the Bitcoin price data, let's remove them
bitcoin_data = bitcoin_data[bitcoin_data['Price'] < 100000] # removing values above $100,000

