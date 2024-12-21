

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tweepy

# Define function to scrape Coindesk website for latest news headlines related to Tether and Rumble
def scrape_news():
    # Get Coindesk website
    url = "https://www.coindesk.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # Identify news section
    news_section = soup.find("section", {"class": "homepage-featured-articles"})
    # Get all news headlines
    news_headlines = news_section.find_all("h3", {"class": "heading"})
    # Loop through headlines to find relevant headline
    for headline in news_headlines:
        # Check if headline contains both Tether and Rumble
        if "Tether" in headline.text and "Rumble" in headline.text:
            # Get headline text and link
            headline_text = headline.text
            headline_link = headline.find("a")["href"]
            break
    return headline_text, headline_link

# Define function to extract relevant information from headline and