

# Import necessary libraries
import re
import requests

# Retrieve headline from Coindesk
response = requests.get('https://www.coindesk.com/michael-saylor-microstrategy-raise-42b-buy-bitcoin').text
headline = re.search("<title>(.*?)</title>", response).group(1)

# Extract relevant information using regular expressions
amount = re.search("\$(\d+\.?\d*)[Bb]", headline).group(1)
timeline = re.search("(\d+)\s(years|months|weeks|days)", headline).group(1)
name = re.search("Michael Saylor|MicroStrategy", headline).group(0)

# Print extracted information
print("1. The involvement of {} in the plans of MicroStrategy to raise funds for buying Bitcoin.".format(name))
print("2. The amount of funds, ${}B, that MicroStrategy plans to raise.".format(amount))
print("3. The timeline of {} years within which the funds will be raised and more Bitcoin will be purchased.".format(timeline))
print("4. The potential impact of this decision on the cryptocurrency market and the overall economy.")
print("5. Any previous actions taken by MicroStrategy in relation to Bitcoin and the potential