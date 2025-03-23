

# Import necessary libraries
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Function to clean and preprocess the text
def preprocess_text(text):
    # Convert all text to lowercase
    text = text.lower()
    # Remove numbers and special characters
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    # Join the tokens back into a string
    preprocessed_text = ' '.join(filtered_tokens)
    return preprocessed_text

# Function to identify key phrases and keywords
def extract_keywords(text):
    # Initialize an empty list for keywords
    keywords = []
    # Tokenize the text
    tokens = word_tokenize(text)
    # Identify keywords based on the given prompt
    for token in tokens:
        if token.lower() == 'sec':
            keywords.append('SEC')
        elif token.lower() == 'crypto' or