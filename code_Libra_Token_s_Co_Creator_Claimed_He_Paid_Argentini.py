

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import spacy
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Read headline and extract key information
headline = "Libra Token’s Co-Creator Claimed He Paid Argentinian President Milei’s Sister"

# Extract co-creator's name
co_creator = headline.split("'")[1]

# Extract payment amount
payment = int(headline.split(" ")[5].replace(",", ""))

# Extract recipient's name
recipient = headline.split(" ")[7] + " " + headline.split(" ")[8]

# Web scraping for co-creator information
co_creator_url = "https://coindesk.com/tag/" + co_creator.lower()
co_creator_response = requests.get(co_creator_url)
co_creator_soup = BeautifulSoup(co_creator_response.text, 'html.parser')

# Extract co-creator's background
co_creator_bio = co_creator_soup.find("div", {"class": "author-bio"}).text.strip()

# Extract co-creator's current position
co_creator_position = co_creator_soup.find("div", {"class": "author-bio"}).find("p").text.strip()

# Web scraping for recipient information
recipient_url = "