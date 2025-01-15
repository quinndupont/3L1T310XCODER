

# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary resources for NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Define the headline
headline = "Crypto Daybook Americas: XRP, AI Coins Eye Big Moves While Bitcoin in Stasis Ahead of CPI"

# Tokenize the headline
tokens = word_tokenize(headline)

# Remove stop words from the tokens
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if not w in stop_words]

# Lemmatize the filtered tokens
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]

# Initialize empty lists for different elements in the headline
cryptocurrencies = []
status = ""
events = []

# Loop through the lemmatized tokens to extract key information
for token in lemmatized_tokens:
    # Identify cryptocurrencies mentioned
    if token.isupper() and token != "CPI":
        cryptocurrencies.append(token)
    # Identify current status
    if