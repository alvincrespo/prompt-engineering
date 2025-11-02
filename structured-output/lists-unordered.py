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
Generate an unordered list containing ONLY the names of the top 5 cities to visit in 2026.
"""

response = get_response(prompt)
print(response)

# Output:
# - Tokyo
# - Barcelona
# - New York City
# - Sydney
# - Cape Town
