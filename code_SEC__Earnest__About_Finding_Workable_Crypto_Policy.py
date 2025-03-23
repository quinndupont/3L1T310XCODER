

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Define function to scrape Coindesk article
def scrape_coindesk(url):
    """
    This function takes in a Coindesk article URL and returns the article content as a string.
    """
    # Make request to Coindesk article URL
    response = requests.get(url)
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all paragraph tags (p) that contain article content
    article = soup.find_all('p')
    # Convert article content to string
    article_str = ' '.join([paragraph.get_text() for paragraph in article])
    # Return article content
    return article_str

# Define function to analyze sentiment of article
def analyze_sentiment(text):
    """
    This function takes in a string of text and uses the NLTK Vader sentiment analyzer to determine the sentiment score.
    Returns a positive, neutral, or negative sentiment based on the compound score.
    """
    # Instantiate Vader sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    # Analyze sentiment of text
    sentiment = sid.polarity_scores(text