

# Import necessary libraries
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
from textblob import TextBlob

# Define function to parse headline and extract relevant information
def analyze_headline(headline):
    # Split headline into words
    words = headline.split(" ")
    
    # Extract event name, speaker name, and year
    event_name = words[0]
    speaker_name = words[1]
    year = words[-1]
    
    # Return extracted information
    return event_name, speaker_name, year

# Use spaCy for tokenization and POS tagging
nlp = spacy.load('en_core_web_sm')
def get_pos_tags(headline):
    # Tokenize headline
    doc = nlp(headline)
    
    # Get POS tags for each word
    pos_tags = [(token.text, token.pos_) for token in doc]
    
    # Return list of POS tags
    return pos_tags

# Use NLTK's VADER for sentiment analysis
analyzer = SentimentIntensityAnalyzer()
def get_sentiment_scores(headline):
    # Perform sentiment analysis on headline
    sentiment_scores = analyzer.polarity_scores(headline)
    
    # Get polarity and subjectivity scores