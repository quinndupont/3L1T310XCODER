

# Import necessary libraries
import requests # for making HTTP requests
from bs4 import BeautifulSoup # for web scraping
import pandas as pd # for data analysis and manipulation
from textblob import TextBlob # for sentiment analysis
import matplotlib.pyplot as plt # for data visualization


# Function to scrape news headlines from Coindesk for a given date range
def scrape_headlines(start_date, end_date):
  # Initialize an empty list to store headlines
  headlines = []

  # Define the base URL for Coindesk news
  base_url = "https://www.coindesk.com/"

  # Loop through all dates in the given range
  for date in pd.date_range(start_date, end_date):
    # Format the date as YYYY/MM/DD for the URL
    url_date = date.strftime("%Y/%m/%d")

    # Make a GET request to the URL
    response = requests.get(base_url + url_date)

    # Parse the HTML response
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all headlines with class "fade"
    headlines_list = soup.find_all(class_="fade")

    # Append each headline to the list
    for headline in headlines_list:
      headlines.append(headline.text)

 