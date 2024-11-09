

# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.chunk import ne_chunk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import requests
from bs4 import BeautifulSoup

# Define function to preprocess text
def preprocess(text):
    # Remove unnecessary characters and convert to lowercase
    clean_text = "".join(c for c in text if c not in ('!', '?', ',', '.', ':', ';', '"')).lower()
    return clean_text

# Define function to extract keywords and phrases
def extract_keywords(text):
    # Tokenize text
    tokens = word_tokenize(text)
    # Tag words with part-of-speech tags
    tagged_tokens = pos_tag(tokens)
    # Filter out stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [w for w in tagged_tokens if not w[0] in stop_words]
    # Extract keywords and phrases
    keywords = []
    for token in filtered_tokens:
        # Check if word is a noun or adjective
        if token[1] == "NN" or token[1] == "JJ":
            # Add to keywords list
            keywords.append(token