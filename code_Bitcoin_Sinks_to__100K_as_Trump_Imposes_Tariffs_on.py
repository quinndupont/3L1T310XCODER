 

# Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords

# Function to extract keywords from headline
def extract_keywords(headline):
    # Tokenize headline
    tokens = word_tokenize(headline)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if not word in stop_words]
    # Tag tokens with part-of-speech
    tagged_tokens = pos_tag(filtered_tokens)
    # Extract relevant keywords
    keywords = [word for word, pos in tagged_tokens if pos == 'NNP' or pos == 'NNPS']
    return keywords

# Function to retrieve historical data on Bitcoin price
def get_bitcoin_data():
    # API call to retrieve Bitcoin data from CoinMarketCap
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
    # Convert response to JSON
    data = response.json()
    # Convert JSON to dataframe
    df = pd.DataFrame(data)
    # Convert 'price_usd' column to float
    df['price_usd'] = df['price_usd'].astype(float