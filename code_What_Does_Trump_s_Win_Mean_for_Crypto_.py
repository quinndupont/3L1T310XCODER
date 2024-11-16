

# Import necessary libraries
import nltk
import spacy
import requests
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Gather dataset of news articles and social media posts
# Define list of sources to scrape data from
sources = ['https://www.coindesk.com/', 'https://www.bloomberg.com/', 'https://twitter.com/']

# Define function to scrape data from sources and return a list of articles and posts
def scrape_data(sources):
    data = []
    for source in sources:
        # Use requests library to get HTML from source
        req = requests.get(source)
        # Use BeautifulSoup to parse HTML
        soup = BeautifulSoup(req.content, 'html.parser')
        # Use CSS selectors to find relevant content
        articles = soup.select('h3 a')
        posts = soup.select('p')
        # Append content to data list
        for article in articles:
            data.append(article.text)
        for post in posts:
            data.append(post.text)
    return data

# Pre