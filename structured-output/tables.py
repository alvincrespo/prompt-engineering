from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads .env file automatically

client = OpenAI()  # uses OPENAI_API_KEY from env

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
prompt = """"
Generate a table containing 5 movies I should watch if I love horror films. The columns should be: Movie Title and Rating.
"""

response = get_response(prompt)
print(response)

# Output:
# Here’s a table of 5 horror films you might enjoy, along with their ratings:

# | Movie Title                     | Rating  |
# |---------------------------------|---------|
# | Hereditary                      | 7.3/10  |
# | The Conjuring                   | 7.5/10  |
# | Get Out                         | 7.7/10  |
# | A Quiet Place                   | 7.5/10  |
# | Midsommar                       | 7.1/10  |
