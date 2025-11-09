from utils.openai_client import get_response

text = "Once upon a time in a quaint little village, there lived a curious young boy named David. David was [...]"

instructions = "You will be provided with a text delimited by triple backticks. Generate a suitable title for it."

output_format = """
Use the following format for the output:
- Text: <text we want to generate>
- Title: <the generated title>
"""

prompt = instructions + output_format + f"```{text}```"

print(get_response(prompt))

# Output:
# - Text: Once upon a time in a quaint little village, there lived a curious young boy named David. David was [...]
# - Title: The Adventures of Curious David in a Quaint Village
