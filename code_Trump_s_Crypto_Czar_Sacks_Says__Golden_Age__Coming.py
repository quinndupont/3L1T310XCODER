

# Importing necessary libraries
import re

# Defining the headline and news source variables
headline = "Trump's Crypto Czar Sacks Says 'Golden Age' Coming"
news_source = input("Please enter the news source: ")

# Extracting relevant information from the headline using regular expressions
name = re.search(r"Trump's Crypto Czar (\w+)", headline).group(1)
statement = re.search(r"Says '(.*)'", headline).group(1)

# Printing the extracted information
print("Name of the person mentioned in the headline:", name)
print("Statement made by the person:", statement)

# Analyzing the statement made by the 'Crypto Czar'
if statement == 'Golden Age':
    print("The predicted 'Golden Age' could potentially have a positive impact on the cryptocurrency market.")
else:
    print("The statement made by the 'Crypto Czar' does not suggest any major impact on the cryptocurrency market.")

# Providing insights based on the selected news source
if news_source == 'CoinDesk':
    print("According to CoinDesk, the 'Golden Age' could refer to a period of increased adoption and mainstream acceptance of cryptocurrencies.")
elif news_source == 'Coin Telegraph':
    print("Coin Telegraph suggests that the '