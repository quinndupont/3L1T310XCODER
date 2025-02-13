

# Import necessary libraries
import spacy

# Load English language model
nlp = spacy.load('en_core_web_sm')

# Define headline to be analyzed
headline = 'El Salvador Dispatch: Berlín, the Bitcoin Marvel Hidden in the Mountains'

# Perform NLP on headline
doc = nlp(headline)

# Extract main subject of the headline
main_subject = doc[0:2]

# Print main subject
print('Main subject of the headline: ', main_subject)

# Identify location mentioned in the headline
for token in doc:
    if token.ent_type_ == 'GPE': # GPE refers to geopolitical entity
        location = token

# Print location mentioned
print('Location mentioned in the headline: ', location)

# Recognize mention of Bitcoin
for token in doc:
    if token.text == 'Bitcoin':
        bitcoin_mention = token

# Print Bitcoin mention
print('Bitcoin mention: ', bitcoin_mention)

# Understand connotation of 'marvel'
for token in doc:
    if token.text == 'marvel':
        marvel_connotation = token

# Print connotation of 'marvel'
print('Connotation of "marvel": ', marvel_connotation)

# Analyze relationship between Bitcoin