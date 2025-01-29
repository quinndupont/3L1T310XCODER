

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define variables for Ondo Finance's offering and XRP Ledger
ondo_offering = 185000000  # $185M
xrp_ledger = 'XRP Ledger'

# Gather data on Ondo Finance's tokenized U.S. Treasury offering
# In this example, we will use hypothetical data
offering_amount = ondo_offering
token_type = 'security tokens'
target_audience = 'institutional investors'

# Print information about the offering
print("Ondo Finance's tokenized U.S. Treasury offering:")
print("Amount: $" + str(offering_amount))
print("Token type: " + token_type)
print("Target audience: " + target_audience)

# Use data from other similar offerings to compare with Ondo Finance's offering
# Here, we will use a list of recent tokenized U.S. Treasury offerings
similar_offers = [150000000, 200000000, 175000000, 250000000, 100000000]
avg_offering = sum(similar_offers) / len(similar_offers)  # Calculate average offering amount

# Print comparison information
print("\