

# Import necessary libraries
import re
import requests
from bs4 import BeautifulSoup

# Define variables
headline = ''
country = ''
regulator = ''
statement = ''
revolution = ''

# Make HTTP request and retrieve headline
url = 'https://www.coindesk.com/el-salvador-crypto-regulator-developing-countries-financial-revolution'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = soup.find('h1').get_text()

# Clean headline
headline = re.sub('[^a-zA-Z\s]', '', headline) # Remove special characters
headline = re.sub('\d+', '', headline) # Remove numbers
headline = headline.strip() # Remove leading and trailing whitespaces
headline = headline.lower() # Convert to lowercase
print(headline)

# Get country
country = re.search('([a-zA-Z]+)\’s', headline).group(1)
print(country)

# Get regulator
regulator = re.search('interview with ([a-zA-Z]+)', headline).group(1)
print(regulator)

# Get statement
statement = re.search('\: (.+)', headline).group(1)
print(statement)

# Get revolution
revolution = re.search('can (.+)$