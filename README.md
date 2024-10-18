# 3L1T310XCODER
Produces coding results.
![All Green Boxes](all_green_boxes.png)

This GitHub Action automates the generation of useful Python code based on headlines from Coindesk. The action scrapes a headline, uses it to prompt an OpenAI language model (via Langchain) to generate an analysis-related code prompt, and then produces a working Python script based on the generated prompt. The resulting code is committed back to the repository once per day at a random time.

## Features
1. Random Execution: The workflow runs once per day, but at a random hour, making it unpredictable.
2. Manual Override: You can manually trigger the workflow to bypass the random check and force a code generation run.
3. Automated Code Generation: Uses OpenAI's language model to generate a code prompt and script based on Coindesk headlines.
4. Automated Commit: The generated code is automatically committed back to the repository.
## How It Works
1. Scheduled Trigger: The workflow is scheduled to run once per hour, but will only proceed once per day at a random time.
2. Random Check: During scheduled runs, a random number is generated, and the action proceeds only if the number matches a specific value, making it unpredictable.
3. Manual Execution: If the workflow is manually triggered, the random check is bypassed.
4. Headline Scraping: The action scrapes a headline from Coindesk.
5. Prompt Generation: The scraped headline is used to generate a prompt for code generation using OpenAI's language model.
6. Code Generation: The model produces a piece of working Python code based on the generated prompt.
7. Commit Changes: The generated code is saved to the repository and automatically committed.
## Configuration
### Prerequisites
OpenAI API Key: You need to have an OpenAI API key to use the language model. Add it as a secret in your GitHub repository:
1. Go to Settings > Secrets and variables > Actions.
2. Click New repository secret.
3. Name the secret OPENAI_API_KEY and add your key.
### Dependencies
The Python script requires the following packages:
- `requests`
- `langchain`
- `openai`
- `beautifulsoup4`
- `langchain_community`
These dependencies are automatically installed by the workflow during execution.
## Workflow Configuration
The workflow is defined in `.github/workflows/daily_random.yml`. The following elements can be customized:
## Schedule:
- Modify the cron expression to change when the workflow runs. Currently, it runs once per hour at minute 0.
- Example: cron: '0 0 * * *' would run it at midnight every day.
## Random Execution:
The workflow randomly decides whether to proceed during a scheduled run. Adjust the RANDOM_NUMBER condition in the script if needed.
## Manual Trigger
You can manually trigger the workflow from the GitHub Actions tab:
1. Go to the Actions tab in your repository.
2. Select Daily Random Code Generation.
3. Click Run workflow and select the desired branch.
## License
This project is licensed under the MIT License.
