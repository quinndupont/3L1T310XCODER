

# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Define function to analyze news articles
def analyze_news_article(article):
    # Tokenize headline into separate words
    tokens = word_tokenize(article)
    # Remove stopwords from the tokens
    filtered_tokens = [word for word in tokens if not word in stopwords.words()]
    # Use VADER to determine sentiment of the article
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = sentiment_analyzer.polarity_scores(article)
    # Print sentiment score
    print("Sentiment Score: ", sentiment_scores['compound'])
    # Categorize article based on sentiment score
    if sentiment_scores['compound'] >= 0.05:
        print("Category: News")
    elif sentiment_scores['compound'] <= -0.05:
        print("Category: Opinion")
    else:
        print("Category: Analysis")
    # Extract key words and phrases related to cryptocurrency and blockchain technology
    key_words = []
    for token in filtered_tokens:
        if token.lower() == "cryptocurrency" or token.lower() == "blockchain" or token.lower() == "bitcoin