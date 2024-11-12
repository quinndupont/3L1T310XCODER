

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Gather data
bitcoin_data = pd.read_csv('bitcoin_data.csv') # Replace with actual file name and path

# Clean and format data
bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date']) # Convert date column to datetime format
bitcoin_data.set_index('Date', inplace=True) # Set date column as index
bitcoin_data.sort_index(inplace=True) # Sort data by date in chronological order

# Calculate percentage increase in value
current_price = bitcoin_data['Price'].iloc[-1] # Get current price from last row
past_week_price = bitcoin_data['Price'].iloc[0] # Get price from first row
percentage_increase = (current_price - past_week_price) / past_week_price * 100 # Calculate percentage increase

# Create line graph
plt.plot(bitcoin_data['Price']) # Plot price data as line graph
plt.title('Bitcoin Price Movement in the Past Week') # Add title
plt.xlabel('Date') # Add x-axis label
plt.ylabel('Price (USD)') # Add y-axis label
plt.show() # Display graph

# Display results
print('Current Bitcoin price: