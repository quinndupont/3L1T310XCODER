

# Import necessary libraries for natural language processing
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Define the headline to be analyzed
headline = "El Salvador Dispatch: Searching for Bitcoin City, the Modern El Dorado"

# Extract key themes and topics from the headline using word tokenization
tokens = word_tokenize(headline)

# Create a list of stop words to be removed from the tokens
stop_words = set(stopwords.words('english'))

# Remove stop words from the tokens
filtered_tokens = [word for word in tokens if not word in stop_words]

# Perform lemmatization on the remaining tokens to reduce them to their root form
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# Identify key themes and topics by looking for specific words and phrases
location = [word for word in lemmatized_tokens if word == "El" or word == "Salvador"]
concept = [word for word in lemmatized_tokens if word == "Bitcoin" or word == "City"]
comparison = [word for word in lemm