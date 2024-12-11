

# Import necessary libraries
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Define function for data collection
def data_collection():
    # Get Coindesk's list of "Most Influential 2024"
    url = 'https://www.coindesk.com/most-influential-2024'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Create empty lists for storing data
    names = []
    titles = []
    companies = []
    social_media = []
    news_mentions = []

    # Scrape data from website
    for row in soup.find_all('div', class_='influencer-item'):
        # Get name
        name = row.find('h2').text
        names.append(name)

        # Get title
        title = row.find('p', class_='influencer-title').text
        titles.append(title)

        # Get company
        company = row.find('p', class_='influencer-company').text
        companies.append(company)

        # Get social media followers
        social_media_url = row.find('ul', class_='