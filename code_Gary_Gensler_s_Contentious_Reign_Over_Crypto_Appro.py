

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Define function for sentiment analysis
def get_sentiment(text):
    # Instantiate SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    # Calculate polarity scores of the text
    sentiment = sia.polarity_scores(text)
    # Return sentiment label
    return sentiment['compound']

# Load data from different sources
sec_announcements = pd.read_csv('sec_announcements.csv')
news_articles = pd.read_csv('news_articles.csv')
social_media_posts = pd.read_csv('social_media_posts.csv')

# Merge all data into one dataframe
crypto_data = pd.concat([sec_announcements, news_articles, social_media_posts])

# Clean and preprocess data
crypto_data['text'] = crypto_data['text'].apply(lambda x: x.lower())
crypto_data['sentiment'] = crypto_data['text'].apply(get_sentiment)

# Plot sentiment analysis results
sns.set_style('darkgrid')
plt.figure(figsize=(10,8))
sns.histplot(data=crypto_data, x='sentiment', bins=