

# Import necessary libraries
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Function to gather data from SEC announcements and press releases
def collect_data():
    # Set base url for SEC website
    base_url = "https://www.sec.gov/"
    
    # Get all press releases related to cryptocurrency enforcement
    press_releases = requests.get(base_url + "cgi-bin/browse-edgar?action=getcurrent&type=8-K&company=&dateb=&owner=exclude&start=0&count=100&output=atom")
    
    # Get all enforcement actions related to cryptocurrency
    enforcement_actions = requests.get(base_url + "cgi-bin/browse-edgar?action=getcurrent&type=8-K&company=&dateb=&owner=exclude&start=0&count=100&output=atom")
    
    # Get all policy changes related to cryptocurrency
    policy_changes = requests.get(base_url + "cgi-bin/browse-edgar?action=getcurrent&type=8-K&company=&dateb=&owner=exclude&start=0&count=100&output=atom")
    
    # Convert data to JSON format
   