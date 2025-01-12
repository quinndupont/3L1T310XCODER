

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import gensim
from gensim import corpora, models

# 1. Retrieve the headline from Coindesk's website using web scraping techniques.
# Make a GET request to Coindesk's website
url = 'https://www.coindesk.com/'
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the headline element and get the text
headline = soup.find('h3', class_='heading')

# Print the headline
print("Headline:", headline.text)

# 2. Preprocess the headline by removing punctuation, converting all letters to lowercase, and removing stop words.
# Convert the headline to lowercase
headline = headline.text.lower()

# Remove punctuation from the headline
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
headline = ''.join(char for char in headline if char not in punctuations)

