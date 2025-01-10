

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the job market data for the month of December
job_data = pd.read_csv("december_job_data.csv")

# Calculate the difference between the actual number of jobs added and the estimated number of jobs
actual_jobs_added = 256000
estimated_jobs_added = 160000
difference = actual_jobs_added - estimated_jobs_added

# Print the difference and determine if the job market performance was better or worse than expected
print("The difference between the actual number of jobs added and the estimated number of jobs is: ", difference)
if difference > 0:
    print("The job market performance for the month of December was better than expected.")
elif difference == 0:
    print("The job market performance for the month of December was as expected.")
else:
    print("The job market performance for the month of December was worse than expected.")

# Determine which industries or sectors saw the most job growth and which ones were the least affected
job_types = job_data['Job Type']
job_locations = job_data['Job Location']
job_growth = {}

# Loop through the job types and locations to count the number of jobs in each industry and location
for i in range(len