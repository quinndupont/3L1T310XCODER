

#Importing necessary modules
import re #Regular expression module for text parsing

#Defining the function to extract and analyze key information from the Coindesk headline
def analyze_coindesk_headline(headline):
    
    #Using regular expression to extract relevant information from the headline
    company_name = re.search(r'\b[A-Z][a-z]+\b', headline).group() #Extracting the first capitalized word as the company name
    cryptocurrency = re.search(r'\b[a-z]+\b', headline).group() #Extracting the first lowercase word as the type of cryptocurrency mentioned
    windfall = re.search(r'\$\d+(\.\d+)?B', headline).group() #Extracting the windfall amount in USD
    action = re.search(r'(?<=After ).+(?= Stablecoin)', headline).group() #Extracting the action taken by the company
    source = re.search(r'(?<=source of the headline, ).+', headline).group() #Extracting the source of the headline
    
    #Printing the extracted information
    print("Company Name: " + company_name)
    print("Type of Cryptocurrency: " + cryptocurrency)
    print("Windfall Amount: " + windfall)
   