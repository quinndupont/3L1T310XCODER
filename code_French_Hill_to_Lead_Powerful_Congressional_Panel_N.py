

# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import ne_chunk
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
import spacy
from spacy import displacy

# Retrieve headline from Coindesk report
url = "https://www.coindesk.com/french-hill-congressional-panel-crypto-term"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = soup.find('h1').text

# Preprocess the headline
headline = headline.lower() # Convert all words to lowercase
tokens = word_tokenize(headline) # Tokenize the headline
stop_words = set(stopwords.words('english')) # Set stopwords
filtered_tokens = [token for token in tokens if token not in stop_words and token.isalpha()] # Remove stopwords and punctuation
preprocessed_headline = ' '.join(filtered_tokens) # Join the tokens back into a string

# Identify keywords and key phrases
keywords = ['french hill', 'congressional panel', 'next term']