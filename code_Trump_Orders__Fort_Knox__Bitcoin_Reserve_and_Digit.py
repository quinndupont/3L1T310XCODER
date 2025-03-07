

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Gather data from news articles and social media
news_data = pd.read_csv('news_articles.csv')
social_data = pd.read_csv('social_media_conversations.csv')

# Merge the two datasets
merged_data = pd.concat([news_data, social_data], ignore_index=True)

# Clean the data by removing unnecessary columns and rows
merged_data = merged_data[['source', 'date', 'text']]
merged_data = merged_data.dropna()

# Perform sentiment analysis using VADER
sid = SentimentIntensityAnalyzer()
merged_data['sentiment'] = merged_data['text'].apply(lambda x: sid.polarity_scores(x)['compound'])

# Visualize sentiment distribution
sns.histplot(data=merged_data, x='sentiment', bins=20, kde=True)
plt.title('Sentiment Distribution of President Trump\'s "Fort Knox" Bitcoin Reserve Order')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Calculate average sentiment score
avg_sentiment = merged_data['sentiment'].