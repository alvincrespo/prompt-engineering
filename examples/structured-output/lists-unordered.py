from utils.openai_client import get_response

prompt = """"
Generate an unordered list containing ONLY the names of the top 5 cities to visit in 2026.
"""

print(get_response(prompt))

# Output:
# - Tokyo
# - Barcelona
# - New York City
# - Sydney
# - Cape Town
