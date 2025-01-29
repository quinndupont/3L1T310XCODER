

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Define function to extract key information from the headline
def extract_info(headline):
  # Convert headline to lowercase and tokenize
  tokens = word_tokenize(headline.lower())
  # Tag tokens with their part of speech
  tagged_tokens = pos_tag(tokens)
  # Initialize variables to store information
  company_name = ''
  offering_amount = ''
  offering_type = ''
  platform = ''
  purpose = ''
  other_keywords = []
  # Loop through tagged tokens to extract information
  for token in tagged_tokens:
    # Look for named entities tagged as 'ORGANIZATION'
    if token[1] == 'ORGANIZATION':
      # Check if company name has already been found
      if company_name == '':
        # Assign company name
        company_name = token[0]
      # If not, check if offering type has already been found
      elif offering_type == '':
        # Assign offering type
        offering_type = token[0]
    # Look for numbers tagged as 'CARDINAL'
    elif token[1] == 'CARDINAL':
      # Check if offering amount