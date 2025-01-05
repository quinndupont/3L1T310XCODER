

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd

# Function for web scraping
def web_scraping(url):
    
    # Send request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the relevant information using CSS selectors
    founders = soup.select('.founders')[0].find_all('a')
    founding_date = soup.select('.date')[0].text
    funding_rounds = soup.select('.funding')[0].find_all('li')
    key_executives = soup.select('.executives')[0].find_all('a')
    partnerships = soup.select('.partnerships')[0].find_all('a')
    
    # Create a dictionary to store the data
    data_dict = {
        'Founders' : [founder.text for founder in founders],
        'Founding Date' : founding_date,
        'Funding Rounds' : [round.text for round in funding_rounds],
        'Key Executives' : [executive.text for executive