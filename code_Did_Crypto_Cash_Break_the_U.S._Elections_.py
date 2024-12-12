

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Define function to scrape news articles and social media posts related to cryptocurrency and U.S. elections
def gather_data(headline):
    # Create empty list to store data
    data = []
    
    # Use web scraping to gather news articles from Google News
    news_url = "https://news.google.com/search?q=cryptocurrency+US+elections&hl=en-US&gl=US&ceid=US%3Aen"
    response = requests.get(news_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract headlines and links from news articles
    headlines = soup.find_all('a', {'class': 'DY5T1d'})
    links = soup.find_all('a', {'class': 'DY5T1d'}, href=True)
    
    # Add headline and link to data list
    for i in range(len(headlines)):
       