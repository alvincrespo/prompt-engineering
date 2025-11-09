from utils.openai_client import get_response

code = """
def compute_average_sales_per_quarter(sales):
  average_sales = sum(sales) / len(sales)
  return average_sales
"""

prompt = f"""
Explain in one sentence what the code delimited by triple backticks does.
```{code}```
"""

response = get_response(prompt)
print(response)

# Output:
# The code defines a function that calculates and returns the average sales from a list of sales figures provided as input.
