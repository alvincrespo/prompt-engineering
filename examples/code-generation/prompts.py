from utils.openai_client import get_response

prompt = f"""
Write a Python function that accepts a list of quarterly sales, and outputs the average sales per quarter. Output only the function code.
"""

response = get_response(prompt)
print(response)

# Output:
# def average_quarterly_sales(sales):
#     if not sales:
#         return 0
#     return sum(sales) / len(sales)
