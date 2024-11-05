

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define function to gather data on each company
def get_company_data(company_name):
    # Create URL for company's Coindesk page
    url = 'https://www.coindesk.com/companies/' + company_name.lower().replace(' ', '-')
    # Send GET request to URL
    response = requests.get(url)
    # Parse response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find company's background information
    background = soup.find('div', class_='company-info').find('p').text
    # Find company's market value
    market_value = soup.find('div', class_='market-value').find('p').text.strip()
    # Find company's involvement in the cryptocurrency industry
    involvement = soup.find('div', class_='involvement').find('p').text.strip()
    
    # Create dictionary with company's data
    company_data = {
        'Company Name': company_name,
        'Background': background,
        'Market Value': market_value,
        'Involvement in Cryptocurrency Industry': involvement
    }
    
    return company_data

# Define function to identify past