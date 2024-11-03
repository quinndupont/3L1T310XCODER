

# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
import re

# Define function to extract relevant information from a news headline
def extract_info(headline):
    # Tokenize headline into words
    words = word_tokenize(headline)
    
    # Remove stopwords and punctuation
    words = [word for word in words if word not in stopwords.words('english') and word.isalpha()]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Identify roles and responsibilities of individuals mentioned in headline
    roles = []
    responsibilities = []
    for word, tag in pos_tag(words):
        if tag == 'NNP' and word != 'Ethereum' and word != 'EigenLayer': # Exclude main keywords
            if re.search(r'\b(co-founder|founder|CEO|CTO|researcher|developer)\b', word, re.IGNORECASE):
                roles.append(word)
            else:
                responsibilities.append(word)
    
    # Identify changes