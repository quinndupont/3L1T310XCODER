

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Scrape the headline from Coindesk's website
url = "https://www.coindesk.com/trump-tariffs-could-affect-bitcoin-ether-dogecoin-prices/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
headline = soup.find("h1", class_="heading heading--xl")
headline = headline.text.strip()

# Clean and preprocess the headline
headline = headline.lower()
headline = headline.replace(".", "")
headline = headline.replace(",", "")
headline = headline.replace("’", "'")
headline = headline.replace("”", "")
headline = headline.replace("“", "")
headline = headline.replace("-", " ")
headline = headline.split()
stop_words = ["the", "of", "on", "a", "an", "could"]
headline = [word for word in headline if word not in stop_words]
headline = " ".join(headline)

# Use VADER to determine the sentiment of the headline
sid = SentimentIntensityAnalyzer()
sentiment_scores = sid.polarity_scores(headline)

# Classify the headline as positive, negative, or neutral
if