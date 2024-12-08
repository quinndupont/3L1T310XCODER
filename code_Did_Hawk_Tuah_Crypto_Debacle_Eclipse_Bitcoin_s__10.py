

# Import necessary libraries

import requests
from bs4 import BeautifulSoup
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
nltk.download('stopwords')
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Define function to retrieve news articles and social media posts related to the events
def get_data():
  
  # Use web scraping techniques to retrieve data from Coindesk website
  url = "https://www.coindesk.com/"
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  
  # Retrieve headlines
  headlines = soup.find_all("h2", {"class": "heading"})
  
  # Search for specific headlines related to the events
  event1 = "Hawk Tuah Crypto Debacle"
  event2 = "Bitcoin's $100K Moment"
  
  # Create empty list to store relevant articles
  articles = []
  
  # Loop through headlines and check if they contain keywords
  for headline in headlines:
    if event1 in headline.text