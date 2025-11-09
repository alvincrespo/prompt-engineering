from utils.openai_client import get_response

prompt = """"
Generate a table containing 5 movies I should watch if I love horror films. The columns should be: Movie Title and Rating.
"""

print(get_response(prompt))

# Output:
# Here’s a table of 5 horror films you might enjoy, along with their ratings:

# | Movie Title                     | Rating  |
# |---------------------------------|---------|
# | Hereditary                      | 7.3/10  |
# | The Conjuring                   | 7.5/10  |
# | Get Out                         | 7.7/10  |
# | A Quiet Place                   | 7.5/10  |
# | Midsommar                       | 7.1/10  |
