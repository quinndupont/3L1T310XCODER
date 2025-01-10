

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from Coindesk headline
df = pd.read_csv('coindesk_job_data.csv')

# Display the data
print("Job data from Coindesk headline:\n")
print(df)

# 1. Total number of jobs added in the U.S. during the month of December
total_jobs_added = df['Actual Jobs Added'].sum()
print("\nTotal number of jobs added in the U.S. during the month of December: {}".format(total_jobs_added))

# 2. Estimated number of jobs that were expected to be added in December
estimated_jobs_added = df['Estimated Jobs Added'].sum()
print("Estimated number of jobs that were expected to be added in December: {}".format(estimated_jobs_added))

# 3. Difference between the actual number of jobs added and the estimated number
difference = total_jobs_added - estimated_jobs_added
print("Difference between the actual number of jobs added and the estimated number: {}".format(difference))

# 4. Percentage increase or decrease in job growth compared to the estimated number
percentage_change = (difference / estimated_jobs_added) * 100
print("Percentage increase or decrease in job growth compared