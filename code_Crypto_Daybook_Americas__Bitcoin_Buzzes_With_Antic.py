

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Define function to scrape headline and extract keywords
def get_keywords(headline):
    # Make GET request to website
    response = requests.get(headline)
    # Create BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract headline text
    headline = soup.find('h1').text
    # Convert headline to lowercase
    headline = headline.lower()
    # Split headline into list of words
    words = headline.split()
    # Define list of relevant keywords
    keywords = ['crypto', 'daybook', 'americas', 'bitcoin', 'buzzes', 'anticipation', 'trump', 'inauguration']
    # Initialize empty list for extracted keywords
    extracted_keywords = []
    # Loop through words in headline and check if they are in list of keywords
    for word in words:
        if word in keywords:
            # Add keyword to extracted_keywords list
            extracted_keywords.append(word)
    # Return extracted keywords
    return extracted_keywords

# Define function to determine sentiment of headline
def get_sentiment(headline):
    # Make GET request to website
    response = requests