

# Import necessary libraries
import re

# Define the headline
headline = "Bitcoin hits $73.5K, just shy of record high"

# Use regular expressions to extract cryptocurrency name
crypto_name = re.search(r'[A-Za-z]+', headline).group()

# Use regular expressions to extract current price
current_price = re.search(r'\$\d+(\.\d+)?K', headline).group()

# Convert current price to float
current_price = float(current_price[1:-1])

# Define previous record high price
previous_record_high = 74.0

# Calculate the difference between current price and previous record high
difference = current_price - previous_record_high

# Calculate the percentage change from previous record high
percent_change = (difference / previous_record_high) * 100

# Display the results
print("- Cryptocurrency Name: " + crypto_name)
print("- Current Price: " + str(current_price) + "K")
print("- Record High: " + str(previous_record_high) + "K")
print("- Difference: " + str(difference) + "K")
print("- Percentage Change: " + str(round(percent_change, 2)) + "%")

# Check if current price is a new record high
if current