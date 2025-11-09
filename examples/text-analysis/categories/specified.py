from utils.openai_client import get_response

text = "I bought your XYZ Smart Watch and wanted to share my positive experience. Impressed with it's sleek design, comfort, and touchscreen usability."

prompt = f"""
Classify the sentiment o the text delimited by triple backticks as positive, negative, or neutral. Give your answer as single word:
```{text}```
"""

print(get_response(prompt))

# Output:
# positive
