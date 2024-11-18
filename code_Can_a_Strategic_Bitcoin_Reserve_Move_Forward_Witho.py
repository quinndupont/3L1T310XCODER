

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define function to extract key information from headline
def extract_info(headline):
    # Split headline into individual words
    words = headline.split()
    # Initialize variables for potential impact of strategic Bitcoin reserve and Congress involvement
    reserve = False
    congress = False
    # Iterate through words to check for keywords
    for word in words:
        if word.lower() == "strategic" or word.lower() == "reserve":
            reserve = True
        if word.lower() == "congress":
            congress = True
    # Return boolean values for reserve and congress
    return reserve, congress

# Define function for sentiment analysis
def sentiment_analysis(headline):
    # Initialize Sentiment Intensity Analyzer
    sia = SentimentIntensityAnalyzer()
    # Perform sentiment analysis on headline
    sentiment = sia.polarity_scores(headline)
    # Return sentiment score
    return sentiment['compound']

# Define function for web scraping
def web_scraping():
    # Initialize list for expert opinions
    opinions = []
    # Provide