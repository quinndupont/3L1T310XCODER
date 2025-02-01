

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Function to scrape news articles related to Bitcoin from popular sources
def scrape_news():
    # List of news sources to scrape from
    sources = ['https://www.coindesk.com/', 'https://www.cnbc.com/bitcoin/', 'https://www.bloomberg.com/cryptocurrencies']

    # Empty lists to store headlines and articles
    headlines = []
    articles = []

    # Loop through each source
    for source in sources:
        # Get HTML from source
        html = requests.get(source).content

        # Create BeautifulSoup object
        soup = BeautifulSoup(html, 'html.parser')

        # Find all headlines and articles
        for headline in soup.find_all('h3'):
            headlines.append(headline.text)
        for article in soup.find_all('p'):
            articles.append(article.text)

    # Combine headlines and articles into a dataframe
    df = pd.DataFrame({'Headline': headlines, 'Article': articles})

    return df

# Function to perform sentiment analysis on headlines and articles
def sentiment_analysis(df):
    # Initialize