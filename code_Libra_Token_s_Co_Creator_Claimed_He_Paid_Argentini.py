

# Import necessary libraries
import re # for regular expressions
import nltk # for natural language processing
from nltk.sentiment.vader import SentimentIntensityAnalyzer # for sentiment analysis

# Define function to extract data from headline
def extract_data(headline):
    # Use regular expressions to extract names of individuals involved
    names = re.findall(r'Libra Token\'s co-creator|Argentinian President Milei|Milei\'s sister', headline)
    # Use regular expressions to extract action taken
    action = re.findall(r'paid', headline)
    # Use regular expressions to extract context
    context = re.findall(r'Libra Token', headline)

    return names, action, context

# Define function to parse extracted data
def parse_data(names, action, context):
    # Create empty lists to store parsed data
    individuals = []
    roles = []
    sentiment = ""

    # Loop through names to identify individuals and their roles
    for name in names:
        if name == "Libra Token's co-creator":
            individuals.append(name)
            roles.append("co-creator")
        elif name == "Argentinian President Milei":
            individuals.append(name)
            roles.append("president")
        else:
