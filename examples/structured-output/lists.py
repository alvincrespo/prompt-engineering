from utils.openai_client import get_response

prompt = """"
Generate a list containing ONLY the names of the top 5 cities to visit in 2026.
"""

print(get_response(prompt))

# Output:
# 1. Tokyo
# 2. Barcelona
# 3. New York City
# 4. Paris
# 5. Sydney
