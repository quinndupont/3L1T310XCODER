

# Import necessary libraries
import nltk
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import matplotlib.pyplot as plt

# Retrieve headline from Coindesk and store as string variable
headline = "TRUMP and MELANIA Tokens Plunge and Buoy Bitcoin Market on Inauguration Day"

# Clean headline by removing punctuation and converting to lowercase
headline = headline.lower().replace(',', '').replace('.', '')

# Tokenize headline into individual words
tokens = word_tokenize(headline)

# Use named entity recognizer to identify entities mentioned in headline
nlp = spacy.load('en_core_web_sm')
doc = nlp(headline)
entities = [ent.text for ent in doc.ents]

# Use sentiment analyzer to determine overall sentiment of headline
sid = SentimentIntensityAnalyzer()
sentiment_scores = sid.polarity_scores(headline)
sentiment = max(sentiment_scores, key=sentiment_scores.get)

# Use part-of-speech tagger to identify key verbs in headline
pos_tags = pos_tag(tokens)
verbs = [word for word, tag in pos_tags if tag.startswith('VB')]

# Use word embedding model to analyze relationship between key