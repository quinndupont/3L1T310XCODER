

# Import necessary libraries
import re

# Define function to extract relevant data from headline
def extract_data(headline):
    # Use regular expressions to find numerical data
    prices = re.findall(r'\$([\d\.]+)K', headline)
    # Convert values to numerical data type
    price1 = float(prices[0])
    price2 = float(prices[1])
    # Calculate price difference
    price_change = price2 - price1
    # Check if change is positive or negative
    if price_change < 0:
        print("Bitcoin has crashed by ${}K".format(abs(price_change)))
    else:
        print("Bitcoin has surged by ${}K".format(price_change))
    # Extract timestamp from headline
    timestamp = re.findall(r'From\s([a-zA-Z\s]+)', headline)[0]
    # Return timestamp for future analysis
    return timestamp

# Create dictionary to track volatility of Bitcoin prices
volatility = {}

# Example headline
headline = "Bitcoin Crashed Below $94K in Sudden Plunge From Record Perch Around $100K"

# Extract data and store in dictionary
timestamp = extract_data(headline)
volatility[timestamp] = extract_data(headline)

