from utils.openai_client import get_response

text = "In the heart of the forest, sunlight filters through the lush green canopy, creating a tranquil atmosphere."

prompt = f"""
You will be provided with a text delimited by triple backticks.
If the text is written in English, check if it contains the keyword 'technology'.
If it does, suggest a suitable title for it, otherwise, write 'Keyword not found'.
```{text}```
"""

print(get_response(prompt))

# Output:
# Keyword not found
