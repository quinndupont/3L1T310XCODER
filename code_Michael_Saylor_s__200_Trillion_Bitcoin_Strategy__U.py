

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import re
import nltk

# Prompt user to input the Coindesk article URL
url = input("Please input the URL of the Coindesk article containing the headline: ")

# Use requests library to get the HTML content of the article
r = requests.get(url)

# Use BeautifulSoup to extract the text from the article
soup = BeautifulSoup(r.content, 'html.parser')
article_text = soup.get_text()

# Use regular expressions to search for relevant keywords and phrases
michael_saylor_count = len(re.findall('Michael Saylor', article_text))
trillion_count = len(re.findall('\$200 trillion', article_text))
strategy_count = len(re.findall('Bitcoin strategy', article_text))
domination_count = len(re.findall('U.S. BTC domination', article_text))
immortality_count = len(re.findall('immortality', article_text))

# Print the counts and locations of the keywords
print("Number of times 'Michael Saylor' appears in the article: ", michael_saylor_count)
print("Number of times '$200 trillion' appears in the article: ", trillion_count)
print("Number of times 'Bitcoin strategy' appears in the article: ", strategy_count)
print("