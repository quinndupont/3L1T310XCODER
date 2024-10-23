

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Set up dataframe
df = pd.DataFrame(columns = ['Headline', 'Author', 'Content'])

# Scrape Coindesk's article on Gensler and Wilson
url = "https://www.coindesk.com/gary-gensler-don-wilson-cftc-crypto"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Get headline, author, and content
headline = soup.find('h1').text
author = soup.find('div', class_='author-row').find('a').text
content = soup.find('div', class_='article-content-container').text

# Add data to dataframe
df.loc[0] = [headline, author, content]

# Scrape data on Gensler and Wilson
gensler_url = "https://www.sec.gov/biography/gary-gensler"
wilson_url = "https://www.theocc.com/about/newsroom/articles/donald-wilson-bio.jsp"

gensler_page = requests.get(g