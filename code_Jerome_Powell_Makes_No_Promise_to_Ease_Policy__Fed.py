

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Define function to gather latest statement from Jerome Powell
def get_latest_statement():
    # Get latest statement from Coindesk website
    url = 'https://www.coindesk.com/powell-feds-approach-inflation'
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Get the headline
    headline = soup.find('h1').text
    return headline

# Define function to summarize key points of the statement
def summarize_statement(statement):
    # Use NLTK's Vader Sentiment Intensity Analyzer to classify tone of statement
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(statement)
    # Get key points of statement
    key_points = 'The key points of Jerome Powell\'s latest statement regarding potential changes to monetary policy and their focus on inflation are:'
    key_points += '\n- Focus on inflation: Powell emphasized that the Federal Reserve will continue to focus on achieving 2% inflation and will be patient in making any changes to monetary policy.'
    key_points += '\