

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define function to scrape SEC roundtable discussion transcript
def scrape_transcript(url):
  # Make request to SEC website
  response = requests.get(url)
  # Parse HTML data using BeautifulSoup
  soup = BeautifulSoup(response.text, 'html.parser')
  # Find all the statements made by commissioners
  statements = soup.find_all('p', class_='cm')
  # Create an empty dictionary to store statements and their corresponding level of seriousness
  statement_dict = {}
  # Loop through all the statements
  for statement in statements:
    # Convert statement to lowercase for easier comparison
    statement = statement.text.lower()
    # Check if statement contains any key words or phrases indicating seriousness or urgency
    if 'earnest' in statement or 'serious' in statement or 'urgent' in statement or 'determined' in statement:
      # Add statement to dictionary with a corresponding level of seriousness
      statement_dict[statement] = 'Serious'
    else:
      # Add statement to dictionary with a corresponding level of seriousness
      statement_dict[statement] = 'Neutral'
  # Return statement dictionary
  return statement_dict

# Define function to analyze the context of statements and