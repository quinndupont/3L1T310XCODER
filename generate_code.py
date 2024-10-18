import os
import requests
from bs4 import BeautifulSoup
from langchain.llms import OpenAI

def get_coindesk_headline():
    url = 'https://www.coindesk.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Try to find the first headline
    headline_tag = soup.find('h4')
    if not headline_tag:
        headline_tag = soup.find('h3')
    if not headline_tag:
        headline_tag = soup.find('h2')
    if headline_tag:
        headline = headline_tag.get_text().strip()
        return headline
    else:
        return None

def main():
    headline = get_coindesk_headline()
    if not headline:
        print("Failed to get headline from Coindesk.")
        return
    print(f"Headline: {headline}")

    # Initialize the LLM
    llm = OpenAI(temperature=0.7)

    # Generate the prompt for code generation
    prompt_generation_prompt = f"Given the following headline from Coindesk: '{headline}', generate a detailed prompt for creating a useful piece of code that can analyze the subject matter of the headline. The prompt should be appropriate to produce code that helps analyze or understand the topic of the headline."
    code_prompt = llm(prompt_generation_prompt)

    print(f"Code Prompt: {code_prompt}")

    # Generate the code based on the code_prompt
    code_generation_prompt = f"Write a Python script that fulfills the following prompt: '{code_prompt}'. Make sure the code is functional and includes necessary imports and comments."
    code = llm(code_generation_prompt)

    print("Generated Code:")
    print(code)

    # Save the code to a file
    safe_headline = ''.join(c if c.isalnum() or c in (' ','.','_') else '_' for c in headline)
    filename = f"code_{safe_headline[:50].replace(' ','_').replace('/','_')}.py"
    with open(filename, 'w') as f:
        f.write(code)
    print(f"Code saved to {filename}")

if __name__ == '__main__':
    main()
