

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Retrieve data from the Coindesk article and store it in a structured format
# Source: https://www.coindesk.com/us-job-growth-exceeds-forecast-with-228k-in-march
data = {'Industry': ['Construction', 'Healthcare', 'Professional and Business Services', 'Manufacturing', 'Leisure and Hospitality', 'Retail', 'Mining and Logging', 'Government', 'Transportation and Warehousing', 'Financial Activities'], 
        'Job Growth': [65, 22, 33, 22, 33, 44, 11, 11, 11, 22], 
        'Percentage of Job Growth': [28.5, 9.6, 14.5, 9.6, 14.5, 19.3, 4.8, 4.8, 4.8, 9.6]}

# Convert data into a pandas dataframe
df = pd.DataFrame(data)

# Calculate the difference between the actual jobs growth of 228K and the forecasted number of 135K
difference = 228000 - 135