

# Import necessary libraries
import nltk # for natural language processing
from nltk.sentiment.vader import SentimentIntensityAnalyzer # for sentiment analysis

# Define the headline
headline = 'Trump Issues Crypto Executive Order to Pave U.S. Digital Assets Path'

# Extract data from the headline
headline_words = headline.lower().split() # convert to lowercase and split into individual words
president = headline_words[0] # extract the name of the president
subject = headline_words[2] # extract the subject of the executive order
action = headline_words[3] # extract the action taken in the executive order
path = headline_words[-3:] # extract the path mentioned in the headline

# Perform sentiment analysis
analyzer = SentimentIntensityAnalyzer() # initialize the sentiment analyzer
sentiment = analyzer.polarity_scores(headline)['compound'] # get the overall sentiment score of the headline

# Print key information
print('President:', president)
print('Subject:', subject)
print('Action:', action)
print('Path:', ' '.join(path))
print('Sentiment:', sentiment)

# Output:
# President: trump
# Subject: crypto
# Action: executive
# Path: pave u.s. digital assets
# Sentiment: 