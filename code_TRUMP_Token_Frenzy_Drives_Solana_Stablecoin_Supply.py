

# Import necessary libraries and modules
import requests
from bs4 import BeautifulSoup
import tweepy
import pandas as pd
import matplotlib.pyplot as plt

# Define function to retrieve data from Coindesk articles
def get_coindesk_articles():
    # Make a GET request to Coindesk's website
    response = requests.get("https://www.coindesk.com/tag/trump-token")

    # Use BeautifulSoup to parse the HTML response
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all articles with the "trump-token" tag
    articles = soup.find_all("article", class_="article")

    # Create an empty list to store article information
    article_list = []

    # Loop through each article
    for article in articles:
        # Get the title of the article
        title = article.find("h3").text

        # Get the publication date of the article
        date = article.find("time")["datetime"]

        # Get the URL of the article
        url = article.find("a")["href"]

        # Store the information in a dictionary
        article_info = {"title": title, "date": date, "url": url}

        # Append the dictionary to the