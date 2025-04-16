

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
%matplotlib inline

# Create a list of keywords
keywords = ["CoinDesk", "Eric Trump", "headline speaker", "Consensus 2025"]

# Make a GET request to Coindesk website
url = "https://www.coindesk.com/coinsdsk-announces-eric-trump-headline-speaker-consensus-2025"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract relevant information
title = soup.find("h1").get_text()
author = soup.find("span", class_="author-name").get_text()
date_published = soup.find("time")["datetime"]
article_body = soup.find("div", class_="article-content").get_text()

# Define a function to search and extract keywords from article body
def extract_keywords(text, keywords):
    keyword_count = {}
    for keyword in keywords:
        # Use regular expressions to find mentions of keywords
        keyword_count[keyword] = len(re.findall(keyword, text, re.IGNORECASE))
    return keyword_count

# Use the function