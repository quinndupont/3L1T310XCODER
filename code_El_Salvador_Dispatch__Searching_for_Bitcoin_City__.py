

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define function to collect data on El Salvador's decision to adopt Bitcoin
def collect_data():
    # Define API endpoint for government announcements
    url = "https://api.el-salvador.bitcoin.org/api/v1/announcements"
    
    # Make GET request to API endpoint
    response = requests.get(url)
    
    # Check status code
    if response.status_code == 200:
        # Convert response to JSON format
        data = response.json()
        
        # Create empty list to store government announcements
        announcements = []
        
        # Loop through each announcement and extract relevant information
        for announcement in data:
            # Check if announcement is related to Bitcoin adoption
            if "Bitcoin" in announcement["title"]:
                # Append announcement title and content to the list
                announcements.append((announcement["title"], announcement["content"]))
        
        # Return list of announcements
        return announcements
    else:
        # Print error message
        print("Unable to collect data. Please try again later.")

# Define function to collect data on Bitcoin City development plans
def collect_city_data():
    # Define API endpoint for