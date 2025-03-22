

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# Define function to extract statements from given URL
def get_statements(url):
    # Make request to given URL
    response = requests.get(url)
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the <p> tags containing statements
    statements = soup.find_all('p')
    # Create empty list to store statements
    statement_list = []
    # Loop through all <p> tags and extract the text
    for statement in statements:
        statement_list.append(statement.text)
    # Return the list of statements
    return statement_list

# Define function to extract keywords and key phrases from statements
def get_keywords(statements):
    # Create empty list to store keywords
    keywords = []
    # Loop through all statements
    for statement in statements:
        # Tokenize the statement
        tokens = nltk.word_tokenize(statement)
        # Tag the tokens with their part-of-speech
        tagged = nltk.pos_tag(tokens)
        # Loop through tagged