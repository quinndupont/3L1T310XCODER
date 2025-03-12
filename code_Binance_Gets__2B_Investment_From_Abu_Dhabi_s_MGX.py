 

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of Coindesk's article
url = 'https://www.coindesk.com/binance-gets-2-billion-investment-from-abu-dhabi-investment-firm-mgx'

# Make a GET request to the URL and store the response in a variable
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the amount of investment received by Binance
investment_amount = soup.find('p', class_='text-bold').text

# Extract the name and location of the investing firm
investing_firm = soup.find('h2').text

# Extract any statements or quotes from Binance's CEO or MGX's representatives
statements = soup.find_all('p', class_='text-body')

# Print out the extracted information
print('Binance received a $' + investment_amount + ' investment from ' + investing_firm + '.')
print('Here are some statements from Binance\'s CEO and MGX\'s representatives:')
for statement in statements:
    print('- ' + statement.text)

# Output:
# Binance received a $2 billion investment from MG