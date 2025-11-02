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

text = "In the heart of the forest, sunlight filters through the lush green canopy, creating a tranquil atmosphere."

prompt = f"""
You will be provided with a text delimited by triple backticks.
If the text is written in English, check if it contains the keyword 'technology'.
If it does, suggest a suitable title for it, otherwise, write 'Keyword not found'.
```{text}```
"""

response = get_response(prompt)
print(response)

# Output:
# Keyword not found
