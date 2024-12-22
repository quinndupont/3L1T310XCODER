

# Import necessary libraries
import pandas as pd # for data analysis
import matplotlib.pyplot as plt # for data visualization

# Gather input data
tether_investment = 775000000 # Tether's investment amount in USD
rum_shares_value = 20 # Current value of RUM shares in USD
previous_investments = [500000000, 250000000] # Previous investments in RUM shares in USD
historical_prices = pd.DataFrame({'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01'],
                                  'Price': [15, 18, 22, 25, 30, 35]}) # Historical data of RUM share prices and market trends in USD

# Calculate percentage increase in RUM share value
increase_percentage = (rum_shares_value - historical_prices['Price'].iloc[-1]) / historical_prices['Price'].iloc[-1] * 100
print("The percentage increase in RUM share value is", round(increase_percentage, 2), "%")

# Compare to previous investments and share prices