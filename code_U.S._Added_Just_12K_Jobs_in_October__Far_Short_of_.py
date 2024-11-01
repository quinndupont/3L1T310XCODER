

# Import necessary libraries
import requests
import pandas as pd

# Define function to retrieve employment data for a specific month and year from Bureau of Labor Statistics
def get_employment_data(month, year):
    # Construct the API url with the specified month and year
    url = "https://www.bls.gov/web/empsit/ceshighlights.pdf"
    # Send a GET request to the API
    response = requests.get(url)
    # If the response is successful, extract the data from the response
    if response.status_code == 200:
        # Use pandas to read the response data into a dataframe
        df = pd.read_html(response.content)[0]
        # Set the column names
        df.columns = ["Month", "Year", "Employment Change", "Expected Change"]
        # Filter the dataframe to only include the specified month and year
        df = df[(df["Month"] == month) & (df["Year"] == year)]
        # Extract the employment change and expected change values
        employment_change = df["Employment Change"].values[0]
        expected_change = df["Expected Change"].values[0]
        # Return the employment change and expected change values
        return employment_change, expected