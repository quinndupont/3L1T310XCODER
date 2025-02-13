

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np

# Define function to retrieve news articles from Coindesk
def get_news():
    url = "https://www.coindesk.com/search?q=El+Salvador+Bitcoin"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("article")
    return articles

# Define function to extract key information and insights from articles
def extract_info(articles):
    locations = []
    timelines = []
    motivations = []
    challenges = []
    for article in articles:
        headline = article.find("h2", class_="text-title").text
        location = article.find("div", class_="card-text").text
        locations.append(location)
        timeline = article.find("time").text
        timelines.append(timeline)
        motivation = article.find("p", class_="card-text").text
        motivations.append(motivation)
        challenge = article.find("ul", class_="list-unstyled").text
        challenges.append(challenge)
    return locations, timelines, motivations, challenges

