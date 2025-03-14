

# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Define function to analyze news headline
def analyze_headline(headline):
    # Tokenize headline
    tokens = word_tokenize(headline)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]
    
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    # Identify main subject of headline
    main_subject = lemmatized_tokens[0]
    
    # Determine significance of step taken
    if "first" in lemmatized_tokens and "big" in lemmatized_tokens and "step" in lemmatized_tokens:
        significance = "significant"
    else:
        significance = "not significant"
        
    # Identify specific type of legislation
    if "stablecoin" in lemmatized_tokens or "bill" in lemmatized_tokens:
        legislation = "