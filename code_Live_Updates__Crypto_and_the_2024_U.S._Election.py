

# Step 1: Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 2: Set up the web scraping process
# Make a GET request to Coindesk website and retrieve the HTML data
url = "https://www.coindesk.com/"
r = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

# Extract relevant information such as headlines, article links, and date/time of publication
headlines = []
links = []
dates = []

# Find all <h2> tags with class 'heading'
results = soup.find_all('h2', class_='heading')

# Loop through the results and extract the headlines, links, and dates
for result in results:
    # Extract the headline and remove any leading or trailing spaces
    headline = result.text.strip()
    # Append to the headlines list
    headlines.append(headline)
    
    # Extract the link and append to the links list
    link = result.find('a')['href']
    links.append(link)
    
    # Extract the date and append to the dates list
    date = result.find_next_sibling('div', class_='meta').text.strip()
    dates.append(date)

