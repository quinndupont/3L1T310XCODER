

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import yfinance as yf
import matplotlib.pyplot as plt

# Define function to retrieve latest news articles and updates on partnership
def get_news():
    # Specify URL of news source
    url = "https://www.coindesk.com/search?q=Tether+Rumble"
    
    # Send GET request to retrieve HTML content
    response = requests.get(url)
    
    # Create BeautifulSoup object to parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all news articles on partnership between Tether and Rumble
    articles = soup.find_all('li', {'class': 'post'})
    
    # Create list to store news article titles and links
    news_articles = []
    
    # Loop through the articles and extract title and link
    for article in articles:
        title = article.find('h3').text
        link = article.find('a', {'class': 'fade'}).get('href')
        
        # Append title and link as a tuple to news_articles list
        news_articles.append((title, link))
        
    # Return list of news articles