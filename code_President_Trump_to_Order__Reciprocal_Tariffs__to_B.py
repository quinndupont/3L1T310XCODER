

# Import necessary libraries
import requests
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.corpus import stopwords
from gensim.summarization import keywords
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from transformers import pipeline
import matplotlib.pyplot as plt
import tweepy

# Function to retrieve headline from Coindesk's website and store as string
def get_headline(url):
    # Make GET request to Coindesk's website
    response = requests.get(url)
    # Extract headline from response
    headline = re.findall('<h1 class="heading">(.+?)</h1>', response.text)[0]
    return headline

# Function to preprocess string
def preprocess_string(string):
    # Remove punctuation and extra spaces
    string = re.sub(r'[^\w\s]', '', string)
    string = re.sub(r'\s+', ' ', string)
    # Convert string to lowercase
    string = string.lower()
    return string

# Function to perform sentiment analysis
def sentiment_analysis(string):
    # Initialize Sentiment Intensity Analyzer
    sid = SentimentIntensityAnalyzer()
   