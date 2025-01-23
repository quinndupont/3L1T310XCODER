

# Import necessary libraries
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# Function to extract key entities from the headline
def extract_entities(headline):
    # Split the headline into individual words
    words = headline.split()
    # Initialize an empty list to store the entities
    entities = []
    
    # Loop through the words to extract the entities
    for word in words:
        # Check if the word starts with a capital letter
        if word[0].isupper():
            # Add the word to the entities list
            entities.append(word)
            
    return entities

# Function to determine the relationship between the entities
def determine_relationship(entities):
    # Initialize empty variables to store the entities
    linked_entity = ""
    asset = ""
    purchase_amount = ""
    
    # Loop through the entities list
    for entity in entities:
        # Check for keywords to determine the relationship
        if "Trump-Linked" in entity:
            linked_entity = entity
        elif "TRX" in entity:
            asset = entity
        elif "$" in entity:
            purchase_amount = entity
    
    # Print the relationship between the entities
    print(linked_entity + " is planning to buy more