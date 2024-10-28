

# 1. Import necessary libraries
import requests
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk import ne_chunk

# 2. Define function to retrieve article from Coindesk API
def get_article(headline):
    # API endpoint for Coindesk
    url = "https://api.coindesk.com/v1/articles"
    # Parameters for API call
    parameters = {'headlines': headline}
    # Make API call and store response
    response = requests.get(url, params=parameters)
    # Convert response to JSON format
    json_response = response.json()
    # Return full article
    return json_response['articles'][0]['article']

# 3. Preprocess the article
def preprocess(text):
    # Remove all punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    # Convert all words to lowercase
    lower_tokens = [word.lower() for word in tokens]
    # Remove stop words
    stop_words = stopwords.words('english')
    filtered_tokens = [word for word